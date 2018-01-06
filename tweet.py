# -*- coding: utf-8 -*-

import tweepy
import helper

def getApi(config):
  auth = tweepy.OAuthHandler(config['consumer_key'], config['consumer_secret'])
  auth.set_access_token(config['access_token'], config['access_token_secret'])
  return tweepy.API(auth)

def main():

  config = {}
  execfile("config.py", config)
  api = getApi(config)

  tweet = "Σήμερα γιορτάζουν: " + helper.getAnniversary() + ". #σήμερα #εορτολόγιο"
  status = api.update_status(status=tweet)
  # Yes, tweet is called 'status' rather confusing

if __name__ == "__main__":
  main()
