
from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route("/")
def health():
    return "Webhook is live!"

@app.route("/deploy", methods=["POST"])
def deploy_ad_video():
    try:
        data = request.json
        print("Received data:", data)
        # Simulated hosted video response
        return jsonify({"hosted_link": "https://example.com/generated-dna-video.mp4"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
