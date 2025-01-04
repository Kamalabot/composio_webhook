import json
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/webhook", methods=["POST"])
def webhook():
    if request.method == "POST":
        payload = request.json
        print(json.dumps(payload, indent=2))
        return jsonify(success=True), 200
    return jsonify(success=False), 405


if __name__ == "__main__":
    app.run(debug=False, port=5000, host="0.0.0.0")
