import json
from datetime import date
import tweepy
import pandas as pd

# Authentication
with open("credentials/credentials.json") as json_file:
    credentials = json.load(json_file)

auth = tweepy.OAuthHandler(credentials["consumer_key"], credentials["consumer_secret"])
auth.set_access_token(credentials["access_token"], credentials["access_token_secret"])

api = tweepy.API(auth)

# Get Tweets
QUERY = "#rechazo"
COUNT = 100

public_tweets = api.search(q=QUERY, count=COUNT)

# Tweets to pd.DataFrame
columns = set()
allowed_types = [str, int]
tweets_data = []
for tweet in public_tweets:
    tweet_dict = dict(vars(tweet))
    keys = tweet_dict.keys()
    single_tweet_data = {}
    for k in keys:
        try:
            v_type = type(tweet_dict[k])
        except:
            v_type = None
        if v_type != None:
            if v_type in allowed_types:
                single_tweet_data[k] = tweet_dict[k]
                columns.add(k)
    tweets_data.append(single_tweet_data)

headers_cols = list(columns)

df = pd.DataFrame(tweets_data, columns=headers_cols)

# Export data
today = date.today().isoformat()
df.to_csv(f"data/tweets{today}.csv")
