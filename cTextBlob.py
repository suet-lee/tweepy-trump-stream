from helpers import *

class cTextBlob(object):

	def __init__(self, string):
		self.string = string

	def __str__(self):
		return self.string

	def matchDictionary(self, bias):
		score = 0
		with open('dictionaries/'+bias+'_keywords.txt', 'r') as file:
			for phrase in file.readlines():
				if findPhrase(phrase.strip(), self.string):
					score += 1
		return score

	def getPolarity(self):
		pos = self.matchDictionary('pos')
		neg = self.matchDictionary('neg')
		if pos == 0 and neg == 0:
			return 0
		else:
			score = (pos-neg)/(pos+neg)
			return score

	def getSubjectivity(self):
		high = ['I','my','mine','me']
		med = ['our','we','ours','us']
		low = ['you','they','them','theirs','their']
		subject = {'high': high, 'med': med, 'low': low}
		count = {}
		for key in subject:
			count.update({key: 0})
			for item in subject[key]:
				count[key] += countPhrase(item, self.string)
		sumcount = sum(count.values())
		if sumcount == 0:
			return 0
		else:
			score = (count['high']*0.5 + count['med']*0.35 + count['low']*0.15)/sumcount
			return score

	def sentiment(self):
		polarity = self.getPolarity()
		subjectivity = self.getSubjectivity()
		return {'polarity': polarity, 'subjectivity': subjectivity}
