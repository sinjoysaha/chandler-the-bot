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

    def on_status(self, status):
        if hasattr(status, 'retweeted_status'):
            try:
                tweet = status.retweeted_status.extended_tweet["full_text"]
            except:
                tweet = status.retweeted_status.text
        else:
            try:
                tweet = status.extended_tweet["full_text"]
            except AttributeError:
                tweet = status.text

        description = status.user.description
        loc = status.user.location
        name = status.user.screen_name
        followers = status.user.followers_count
        id_str = status.id_str
        created = status.created_at
        retweet_count = status.retweet_count
        favorite_count = status.favorite_count
        lang = status.lang

        print("Username: \t\t\t" + name)
        print("Description: \t\t\t" + str(description))
        print("location: \t\t\t" + str(loc))
        print("followers: \t\t\t" + str(followers) + "\n\n")
        print("Tweet: \t\t\t" + tweet)
        print("ReTweet Count: \t\t\t" + str(retweet_count))
        print("Favorite Count: \t\t\t" + str(favorite_count))
        print("id_str: \t\t\t" + id_str)
        print("lang: \t\t\t" + lang)
        print("created: \t\t\t" + str(created) + "\n\n\n")
        time.sleep(1)
        return(True)

    def on_error(self, status):
        print(status)
