from flask import Flask, request, jsonify

PORT = 5000

app = Flask(__name__)


@app.route('/_inference', methods=['POST'])
def inference():
    data = request.json
    return jsonify({"message": "Received", "input": data})


if __name__ == '__main__':
    app.run(debug=True, port=PORT)
