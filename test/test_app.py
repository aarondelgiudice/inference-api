import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

import json
import unittest
from flask import Flask
from flask_testing import TestCase

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
        self.assertEqual(
            response.json, {"message": "Received", "input": {"text": "Hello, World!"}}
        )


if __name__ == "__main__":
    unittest.main()
