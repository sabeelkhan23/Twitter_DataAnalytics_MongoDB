# CIS593 - BIG DATA
# SABEEL KHAN, CSUID: 2829233
# LAB3 - TWITTER LOGGING IN MONGO DB
# Reference links used: https://www.earthdatascience.org/courses/use-data-open-source-python/intro-to-apis/twitter-data-in-python/
# https://www.mongodb.com/languages/python#:~:text=The%20first%20step%20to%20connect,text%20editor%20like%20Textpad%2FNotepad.&text=Use%20the%20connection_string%20to%20create,get%20the%20MongoDB%20database%20connection.

from tweepy import Stream
from tweepy import OAuthHandler #For handling authentication
import json #For writing to a JSON file
import tweepy
from pymongo import MongoClient

# Connection to mongodb 

client = MongoClient('mongodb://127.0.0.1:27017/')
db = client['test2']
coll = db['tweets']

# Credentials that are generated in the Twitter developer app

api_key = 'UhKiqm3qCdX6u3Ey3OlD4d7jI'
api_key_secret = 'YpGMrsjPGloocY7EWP82X2u0ELSM2uiodAwHC8YJpmgVwwwgbs'
access_token = '1498409192952115202-dSsKUI6EyYLHiPmN9qsqeSwogzR53V'
access_token_secret = 'sr9BlFw9Oelre09Q83tDrtPxc3V9mnS3letpCn0febuiJ'
class tweepyListen(tweepy.Stream):
 def on_status (self, status):
     json_str = json.dumps(status._json)
     print(json_str) 
     try:
           with open("tweets.json","a") as file: 
              file.write(json_str+",\n")
     except:
           pass
     return True
if __name__ == "__main__":
 listener = tweepyListen(api_key, api_key_secret, access_token, access_token_secret)
 listener.filter(track =['bitcoin', 'CRYPTO'])