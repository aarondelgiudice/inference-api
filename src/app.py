from flask import Flask, request, jsonify
from inference import get_vector

PORT = 5000

app = Flask(__name__)


@app.route("/_inference", methods=["POST"])
def inference():
    data = request.json
    text = data.get("text", "")
    model_name = data.get("model_name", None)
    vector = get_vector(text, model_name)
    return jsonify({"message": "Vector generated", "vector": vector})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=PORT)
