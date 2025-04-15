from flask import Flask, request, jsonify
import tweepy

app = Flask(__name__)

@app.route('/tweet', methods=['POST'])
def post_tweet():
    data = request.get_json()
    tweet_text = data.get('tweet')

    if tweet_text:
        # your existing tweepy logic here
        client.create_tweet(text=tweet_text)
        return jsonify({"status": "Tweet sent"}), 200
    else:
        return jsonify({"error": "No tweet content received"}), 400
