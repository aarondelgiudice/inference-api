import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

import json
import unittest
from flask import Flask
from flask_testing import TestCase
from unittest.mock import patch

from app import app


class TestFlaskApi(TestCase):
    def create_app(self):
        app.config["TESTING"] = True
        return app

    def test_inference_endpoint(self):
        response = self.client.post(
            "/_inference",
            data=json.dumps({"text": "Hello, World!"}),
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn("message", response.json)
        self.assertIn("vector", response.json)

    def test_get_vector(self):
        with patch("src.inference.get_vector") as mock_get_vector:
            mock_get_vector.return_value = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8]

            response = self.client.post(
                "/_inference",
                data=json.dumps({"text": "Hello, World!"}),
                content_type="application/json",
            )

            expected = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8]
            actual = response.json["vector"]
            self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
