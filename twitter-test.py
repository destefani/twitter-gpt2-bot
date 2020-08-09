import json
import tweepy

with open('credentials/credentials.json') as json_file:
    credentials = json.load(json_file)


auth = tweepy.OAuthHandler(credentials['consumer_key'], credentials['consumer_secret'])
auth.set_access_token(credentials['access_token'], credentials['access_token_secret'])

api = tweepy.API(auth)

#Make call on home timeline, print each tweets text
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)