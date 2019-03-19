import tweepy
auth = tweepy.OAuthHandler("consumer_key","consumer_secret")
auth.set_access_token ("access_token", "access_token_secret")
twitter_api = tweepy.API(auth)
cfg_tweets = twitter_api.search(
q = "CodeFirstGirls" #Twitter handle you want to search by
)
for tweet in cfg_tweets:
print tweet.user.name + ": " + tweet.text +"\n"
