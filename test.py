import tweepy
import datetime

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

response = client.create_tweet(text=f"API Test @ {datetime.datetime.now()}")
print(response)

response = client.delete_tweet(id='1702899957722939414')
print(response)
