from flask import Flask, request, jsonify
from flask_cors import CORS
from src.RtcTokenBuilder2 import RtcTokenBuilder, Role_Publisher
import os
from dotenv import load_dotenv

app = Flask(__name__)

# Allow CORS
CORS(app, resources={r"/token/*": {"origins": "http://localhost:5173"}})

load_dotenv()

AGORA_APP_ID = os.getenv("AGORA_APP_ID")
AGORA_APP_CERTIFICATE = os.getenv("AGORA_APP_CERTIFICATE")

TOKEN_EXPIRATION_IN_SECONDS = 3600
PRIVILEGE_EXPIRATION_IN_SECONDS = 3600


@app.route("/token/uid", methods=["GET"])
def get_token_with_uid():
    channel_name = request.args.get("channelName")
    uid = request.args.get("uid", type=int)

    if not channel_name or uid is None:
        return jsonify({"error": "channelName and uid are required"}), 400

    token = RtcTokenBuilder.build_token_with_uid(
        AGORA_APP_ID,
        AGORA_APP_CERTIFICATE,
        channel_name,
        uid,
        Role_Publisher,
        TOKEN_EXPIRATION_IN_SECONDS,
        PRIVILEGE_EXPIRATION_IN_SECONDS
    )

    return jsonify({
        "channelName": channel_name,
        "uid": uid,
        "token": token
    })


@app.route("/token/rtm", methods=["GET"])
def get_token_with_rtm():
    channel_name = request.args.get("channelName")
    account = request.args.get("account")

    if not channel_name or not account:
        return jsonify({"error": "channelName and account are required"}), 400

    token = RtcTokenBuilder.build_token_with_rtm(
        AGORA_APP_ID,
        AGORA_APP_CERTIFICATE,
        channel_name,
        account,
        Role_Publisher,
        TOKEN_EXPIRATION_IN_SECONDS,
        PRIVILEGE_EXPIRATION_IN_SECONDS
    )

    return jsonify({
        "channelName": channel_name,
        "account": account,
        "token": token
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
