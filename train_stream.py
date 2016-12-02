import tweepy
from stream_listener import *
from config import *
import time

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

def get_bias():
	bias = raw_input('Enter bias for filtering tweets (pos/neg): ')
	if bias == 'pos' or bias == 'p':
		return 'pos'
	elif bias == 'neg' or bias == 'n':
		return 'neg'
	else:
		print 'Please enter a valid bias...'
		get_bias()

def get_filters(bias):
	if bias == 'neg':
		return ['notmypresident', 'fucktrump', 'protesttrump', 'antitrump', 'nevertrump']
	elif bias == 'pos':
		return ['fortrump', 'makeamericagreatagain', 'maga', 'trumpwon']

bias = get_bias()
filters = get_filters(bias)
file_to_write = 'data/train_data_'+ bias + '_' + str(int(time.time())) +'.json'

stream_listener = TrainStreamListener(file_to_write, bias, 12000)
stream = tweepy.Stream(auth=api.auth, listener=stream_listener)
stream.filter(track=filters)
