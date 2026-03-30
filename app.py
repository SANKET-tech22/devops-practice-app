from flask import Flask, jsonify
import os
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

@app.route("/")
def home():
    app.logger.info("Home endpoint hit")
    return jsonify({
        "message": "Hello DevOps 🚀",
        "status": "success"
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)