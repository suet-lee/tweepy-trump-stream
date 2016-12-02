from textblob.classifiers import NaiveBayesClassifier
import os
import pickle
import json

data = []

for file in os.listdir('train_data/'):
	with open('train_data/'+ file) as file_data:
		data += json.load(file_data)

with open


# with open('data/')
