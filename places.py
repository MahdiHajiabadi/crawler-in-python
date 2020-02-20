import sys
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import tweepy
import csv
import codecs
from tweepy.api import  API
consumer_key = 'WNqTUVtHsHqtHdU4aZ2TnGZ2X'
consumer_secret= 'nHvgwCHKKE9aFGYYAeUpmd6rS2j13cZGdvOom9mmX7UHP424nL'
access_token = '3943797875-Lme1ZPfpUHLrcxzhmIz4ViLGukIx4ycJ5UMmfZN'
access_token_secret = 'c0Id0Fa8bvqI6PBaRtdRiGFsh9pJreesXpYrH0DaK1lPF'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
#places = api.geo_search(query="USA", granularity="country")
places = api.geo_search(query="IRAN", granularity="country")
place_id = places[0].id

tweets = api.search(q="place:%s" % place_id)

for j in tweets:
    print (str(j.text.encode('ascii','ignore'))+ '|' + str(j.place.country) if j.place else "Undefined Country")
    print('*****************')

