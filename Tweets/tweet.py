import time
import tweepy
import sys,os
import credentials
sys.path.append(os.path.join(os.path.dirname(sys.path[0]), 'blabberbot'))
import blabberbot

INTERVAL = 60*60

auth = tweepy.OAuthHandler(credentials.CONSUMER_KEY,credentials.CONSUMER_SECRET)
auth.set_access_token(credentials.ACCESS_KEY,credentials.ACCESS_SECRET) 
api = tweepy.API(auth)

bot = blabberbot.Blabberbot(blabberbot.celebs["ElonMusk"])

while True:    
    tweet = bot.generate_tweet(140)
    print(tweet)
    api.update_status(tweet)
    time.sleep(INTERVAL)
