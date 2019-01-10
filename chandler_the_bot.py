from tweepy import Stream
from config import *
from functions_on_status import *
from tweepy import OAuthHandler
from tweepy import API

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
api = API(auth)


def postTweet(tweet_this):
    api.update_status(tweet_this)
    print("TWEETED:", tweet_this)


# consumer key, consumer secret, access token, access secret.

# tweet_this = 'Test Tweet 6'
# postTweet(tweet_this)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["#sarcasm", "#sarcastic"])

'''timeline = api.home_timeline()
for time_tweet in timeline:
    print(time_tweet.text)
'''
