import pickle
sys.stdout = open('demo.txt',"w");
from nltk.tokenize import word_tokenize
from textblob.classifiers import NaiveBayesClassifier
cl = pickle.load( open( "classifier.pickle", "rb" ) )
print(cl.classify("text to classify"))
