import tweepy
import json

auth = tweepy.OAuthHandler("y8pta8Dn07uE0oigF6FvKyuKd","5Cge6Y33Lu6adPlh5N8pDj1rTfVx3ELaleEBhyRIb3otwceDXT")
auth.set_access_token ("93611689-6hntzkDRHACfNRTyYhp8uXy8LViT1wU0egEwomjOZ", "zZd1GZYdkY4FD1VtPgxL8WlHzS8mThpNB08ensQnTqyKt")

def getTweets():

    twitter_api = tweepy.API(auth)

    cfg_tweets = twitter_api.search(
        q = "brexit", #Twitter handle you want to search by
        per_page = 18,
    )

    return cfg_tweets

#getTweets()
