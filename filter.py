from tweepy import OAuthHandler
from tweepy import Stream
import tweepy
from tweepy.api import API
# Authentication details. To  obtain these visit dev.twitter.com
consumer_key = 'v6zTWhPzMs1Z6UFK6FizF2aeL'
consumer_secret = '5FA1oymGZwDmqWdlXtb8s8p2x7JWn1PrDBbe3KCRIVhhWyJBMP'
access_token = '3182708354-tRix7hFN57V2RPTQhYOsI58A0qVteqNDOAaOSvL'
access_token_secret = 'qz9ie4TwfVAuXcaIVKtWfnMWUyYp37muqkl82ImtUoEfB'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

class CralingTwitter(tweepy.StreamListener):
    def __init__(self, api=None):
       api = api or API()
        n = 0
        m = 50

    def on_status(self, status):
        print (status.text + '\n')
        n = n+1
        if n < m: return True
        else:
            print ('tweets = '+str(n))
            return False

stream = tweepy.streaming.Stream(auth, CralingTwitter())
stream.filter(track=['Indiana', 'weather'])
