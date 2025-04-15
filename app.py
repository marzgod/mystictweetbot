# app.py

from flask import Flask, request, jsonify
import tweepy
import os

app = Flask(__name__)
print("🚀 Mystic TweetBot started — NO AUTH CHECK PRESENT")

# Tweepy client setup using environment variables
client = tweepy.Client(
    bearer_token=os.getenv("TWITTER_BEARER_TOKEN"),
    consumer_key=os.getenv("TWITTER_API_KEY"),
    consumer_secret=os.getenv("TWITTER_API_SECRET"),
    access_token=os.getenv("TWITTER_ACCESS_TOKEN"),
    access_token_secret=os.getenv("TWITTER_ACCESS_SECRET")
)

# 🧠 This is the webhook route Zapier calls
@app.route('/tweet', methods=['POST'])
def post_tweet():
    # 🔥 NO auth check!
    try:
        data = request.get_json()
        tweet_text = data.get('tweet')

        if not tweet_text:
            return jsonify({"error": "Missing tweet content"}), 400

        client.create_tweet(text=tweet_text)
        return jsonify({"status": "Tweet posted!"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    return 'Mystic Tweet Bot is live 💫', 200
