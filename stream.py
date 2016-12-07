import tweepy
from stream_listener import StreamListener
from config import *
from classify_data import *
import time

def mkdirIfNotExists(path):
	try:
	    os.makedirs(path)
	except OSError:
	    if not os.path.isdir(path):
	        raise

def getStream():
	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

	api = tweepy.API(auth)

	file_to_write = 'data/stream_data_'+ str(int(time.time())) +'.json'
	filters = ['trump', 'donald trump', 'notmypresident', 'maga', 'makeamericagreatagain', 'fortrump', 'protesttrump']
	mkdirIfNotExists('data')

	stream_listener = StreamListener(file_to_write, 60, 10)
	stream = tweepy.Stream(auth=api.auth, listener=stream_listener)
	stream.filter(track=filters)

	createTweetsTable()
	classifyTweets()
