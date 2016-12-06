from textblob.classifiers import NaiveBayesClassifier
from random import shuffle
import os
import pickle
import json

data = []

for file in os.listdir('train_data2/'):
	with open('train_data2/'+ file) as file_data:
		data += json.load(file_data)

# with open('../old/classtrain.json') as fp:
# 	cl = NaiveBayesClassifier(fp)
shuffle(data)
print data

# data = [{'text':'i like', 'label':'pos'},
# {'text':'i hate', 'label':'neg'},
# {'text':'it\'s good', 'label':'pos'},
# {'text':'i quite like it', 'label':'pos'},
# {'text':'terrible things', 'label':'neg'},
# {'text':'something wonderful', 'label':'pos'},
# {'text':'positive vibes', 'label':'pos'},
# {'text':'what a dull time', 'label':'neg'},
# {'text':'pretty solid', 'label':'pos'}]
#
# cl = NaiveBayesClassifier(data)
# print cl
# prob = cl.prob_classify('amazing')
# print prob.max()
# file = open('classifier.pickle', 'wb')
# pickle.dump(object, file)

# with open('data/')
