from flask import Flask, render_template, jsonify, request
import tweepy

app = Flask(__name__)

consumer_key        = "da999O1gnwvZjYx74ujvTs4iO"
consumer_secret     = "y7UaeZ50HRWjTwbyDVN08DLEsC5gSuWXjSkYEXUI3kE4xWLK4K"

access_token        = "2926535838-ZfhwVNQLMHsb0RAtZSk1bae273cfQGCYgnuvLsX"
access_token_secret = "2adsPorxVl2hwS8Lio2ZgZH42MgMVM9hCByUaPOuC4A3C"

client = tweepy.Client(
	consumer_key=consumer_key,
	consumer_secret=consumer_secret,
	access_token=access_token,
	access_token_secret=access_token_secret
)

# Developed by Saharat Saengsawang

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/api/tweet/create', methods=['POST'])
def api_create():
	text = request.json.get('text')
	twitter_response = client.create_tweet(text=text)
	return jsonify(twitter_response)

@app.route('/api/tweet/delete/<tweet_id>', methods=['DELETE'])
def api_delete(tweet_id):
	twitter_response = client.delete_tweet(id=tweet_id)
	return jsonify(twitter_response)

if __name__ == '__main__':
	app.run('0.0.0.0',80,debug=True)





