# dna-ad-webhook
Webhook For Ai Ads
# app.py (Render Webhook)

from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

RUNWAY_API_KEY = "your_runway_api_key"
RUNWAY_GEN_URL = "https://api.runwayml.com/v1/generate"  # Adjust if your endpoint is different

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
        runway_response = requests.post(RUNWAY_GEN_URL, json=payload, headers=headers)
        runway_response.raise_for_status()
        video_url = runway_response.json().get("output", {}).get("url", "Pending...")

        return jsonify({"hosted_link": video_url}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
