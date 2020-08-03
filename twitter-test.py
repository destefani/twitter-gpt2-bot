import json
import tweepy

with open('credentials/credentials.json') as json_file:
    credentials = json.load(json_file)


auth = tweepy.OAuthHandler(credentials['consumer_key'], credentials['consumer_secret'])
auth.set_access_token(credentials['access_token'], credentials['access_secret'])

api = tweepy.API(auth)
