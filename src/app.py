from flask import Flask, request, jsonify
from inference import get_vector

PORT = 5000

app = Flask(__name__)


@app.route('/_inference', methods=['POST'])
def inference():
    data = request.json
    text = data.get("text", "")
    vector = get_vector(text)
    return jsonify({"message": "Vector generated", "vector": vector})


if __name__ == '__main__':
    app.run(debug=True, port=PORT)
