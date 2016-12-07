from textblob import TextBlob
import json
import os
import math
import re
from helpers import *
from cTextBlob import cTextBlob

def collateStreamData():
	data = []
	for file in os.listdir('data/'):
		with open('data/' + file, 'r') as fp:
			data += json.load(fp)
	return data

def unlinkStreamData():
	for file in os.listdir('data/'):
		os.unlink('data/'+ file)

def weightScore(x, level=None):
	if level == 'linear':
		return x
	elif level == 'quad':
		return x**2
	elif level == 'exp':
		return math.exp(x)*x/math.exp(1)
	elif level is None:
		return 1;

def scoreSentiment(text, weight_level=None):
	# returns weighted sentiment score
	blob = TextBlob(text)
	sentiment = blob.sentiment
	if sentiment.polarity != 0:
		polarity = sentiment.polarity
		subjectivity = sentiment.subjectivity
	else:
		cblob = cTextBlob(text)
		sentiment = cblob.sentiment()
		polarity = sentiment['polarity']
		subjectivity = sentiment['subjectivity']
	subj_weight = weightScore(subjectivity, weight_level)
	return polarity*subj_weight

def extractEmotion(tweet):
	# returns list of emotions and scores
	emotions = [{'happy': ['happy','joy','smile','laugh','blessed','joyful']},
				{'sad': ['sad','depressed','unhappy','miserable','upset']},
				{'scared': ['frightened','scared','scary','afraid','nervous','alarmed','worried']},
				{'confused': ['confused','puzzled','questioning','wondering','baffled','bewildered']},
				{'angry': ['angry','rage','disgust','disgusted']},
				{'shocked': ['shock','stunned','astonished','surprised','shocked','dumbfounded']},
				{'hopeful': ['optimistic','confident', 'positive', 'great', 'good', 'congratulations']}]

	score = {'happy': 0, 'sad': 0, 'scared': 0, 'confused': 0, 'angry': 0, 'shocked': 0, 'hopeful': 0}

	for emotion in emotions:
		for adj in emotion:
			if findWholeWord(adj)(tweet):
				score[adj] += 1

	e_list = []

	for key in score:
		if score[key] > 0:
			e_list.append(key)

	return e_list
