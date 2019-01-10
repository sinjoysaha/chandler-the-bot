import json
import time
from tweepy.streaming import StreamListener
from config import *

tweet_dict = {}


def processTweet(tweet_data):
    tweet_dict = json.loads(tweet_data)

    if(not(tweet_dict["lang"] == "en")):
        print("/nTWEET NOT IN ENGLISH/n")
        return

    tweet_time = tweet_dict["created_at"]
    tweet_user_name = tweet_dict["user"]["name"]
    tweet_user_screen_name = tweet_dict["user"]["screen_name"]
    tweet_text = tweet_dict["text"]
    tweet_fulltext = tweet_text

    if(tweet_dict["truncated"]):
        tweet_fulltext = tweet_dict["extended_tweet"]["full_text"]

    if(tweet_text[:4] == 'RT @'):
        tweet_fulltext = tweet_dict["retweeted_status"]["text"]

        if(tweet_dict["retweeted_status"]["truncated"]):
            tweet_fulltext = tweet_dict["retweeted_status"]["extended_tweet"]["full_text"]

    time.sleep(2)
    print()
    print("Time:\t\t\t" + tweet_time)
    print("User Name:\t\t\t" + tweet_user_name)
    print("User Screen Name:\t\t\t@" + tweet_user_screen_name)
    print("Text:\t\t\t" + tweet_text)
    print("Full Text:\t\t\t" + tweet_fulltext)
    print()
    time.sleep(2)


class listener(StreamListener):

    def on_data(self, data):
        print(data)
        processTweet(data)
        return(True)

    def on_error(self, status):
        print(status)
