from flask import Flask, request, jsonify
import tweepy
import os

app = Flask(__name__)

API_KEY = os.environ.get("API_KEY")
API_SECRET = os.environ.get("API_SECRET")
ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.environ.get("ACCESS_TOKEN_SECRET")

auth = tweepy.OAuth1UserHandler(
    API_KEY,
    API_SECRET,
    ACCESS_TOKEN,
    ACCESS_TOKEN_SECRET
)
api = tweepy.API(auth)

@app.route("/tweet", methods=["POST"])
def tweet():
    data = request.json
    tweet_text = data.get("tweet")

    if not tweet_text:
        return jsonify({"error": "No tweet content provided."}), 400

    try:
        api.update_status(status=tweet_text)
        return jsonify({"status": "Tweet posted successfully."})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/")
def home():
    return "Twitter Webhook Bot is running."

if __name__ == "__main__":
    app.run(debug=True)
