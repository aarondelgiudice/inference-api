import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

import json
import unittest
from unittest.mock import patch
from flask_testing import TestCase

from app import app


class TestFlaskApi(TestCase):
    def create_app(self):
        app.config["TESTING"] = True
        return app

    def test_inference_endpoint_structure(self):
        """Test the structure of the inference endpoint's response."""
        response = self.client.post(
            "/_inference",
            data=json.dumps({"text": "Hello, World!"}),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("message", response.json)
        self.assertIn("vector", response.json)

    def test_inference_endpoint_response(self):
        """Test the response of the inference endpoint."""
        # load test cases from test_cases.json file
        with open("test/test_cases.json") as f:
            test_cases = json.load(f)

        for test_case in test_cases:
            with patch("inference.get_vector") as mock_get_vector:
                mock_get_vector.return_value = test_case["vector"]
                response = self.client.post(
                    "/_inference",
                    data=json.dumps({"text": test_case["text"]}),
                    content_type="application/json",
                )
                self.assertEqual(response.status_code, 200)
                self.assertEqual(response.json["message"], "Vector generated")
                self.assertEqual(response.json["vector"], test_case["vector"])


if __name__ == "__main__":
    unittest.main()
