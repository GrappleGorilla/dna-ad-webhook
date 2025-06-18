
import os
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

RUNWAY_API_KEY = os.environ.get("RUNWAY_API_KEY")

@app.route("/")
def health():
    return "DNA Ad Webhook with Runway is live!"

@app.route("/deploy", methods=["POST"])
def deploy_ad_video():
    try:
        data = request.json
        payload = {
            "input": {
                "voiceover": data.get("voiceover"),
                "scenes": data.get("storyboard"),
                "assets": data.get("assets")
            },
            "config": {
                "format": data.get("format", "vertical_mp4"),
                "duration": data.get("duration", "15s")
            }
        }
        headers = {
            "Authorization": f"Bearer {RUNWAY_API_KEY}",
            "Content-Type": "application/json"
        }
        runway_response = requests.post("https://api.runwayml.com/v1/generate", json=payload, headers=headers)
        runway_response.raise_for_status()
        video_url = runway_response.json().get("output", {}).get("url", "Pending...")

        return jsonify({"hosted_link": video_url}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
