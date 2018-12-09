#!/usr/bin/env python
import time
import tweepy
import sys,os
sys.path.append(os.path.join(os.path.dirname(sys.path[0]), 'blabberbot'))
import blabberbot

INTERVAL = 5
"""
CONSUMER_KEY = os.environ['CONSUMER_KEY']
CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
ACCESS_KEY = os.environ['ACCESS_KEY']
ACCESS_SECRET = os.environ['ACCESS_SECRET']
auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY,ACCESS_SECRET) 
api = tweepy.API(auth)
"""
bot = blabberbot.Blabberbot(blabberbot.corpus)

while True:    
    tweet = bot.generate_tweet(140)
    print(tweet)
   # api.update_status(tweet)
    time.sleep(INTERVAL)