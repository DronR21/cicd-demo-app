from flask import Flask, jsonify
import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Hello from my fully automatedCI/CD pipeline!",
        "status": "running",
        "server_time": datetime.datetime.now(datetime.UTC).isoformat()
    })

@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)