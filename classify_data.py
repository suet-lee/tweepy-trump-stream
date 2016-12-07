import json
import os
import MySQLdb
from contextlib import closing
from classify_methods import *
from config import *

def createTweetsTable():
	db = MySQLdb.connect(host=DB_HOST, user=DB_USER, passwd=DB_PASSWD, db=DB_NAME)
	db.set_character_set('utf8mb4')
	try:
		with closing(db.cursor()) as cursor:
			cursor.execute('SET NAMES utf8mb4;')
			cursor.execute('SET CHARACTER SET utf8mb4;')
			cursor.execute('SET character_set_connection=utf8mb4;')
			cursor.execute("CREATE TABLE IF NOT EXISTS tweets (\
							id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,\
							text VARCHAR(255),\
							city VARCHAR(255),\
							country VARCHAR(255),\
							sentiment_raw VARCHAR(10),\
							sentiment_linear VARCHAR(10),\
							sentiment_quad VARCHAR(10),\
							sentiment_exp VARCHAR(10),\
							emotions VARCHAR(255),\
							created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP\
							)")
		db.commit()
	except:
		db.rollback()
		print 'Failed table creation'
	db.close()

def classifyTweets():
	db = MySQLdb.connect(host=DB_HOST, user=DB_USER, passwd=DB_PASSWD, db=DB_NAME)
	db.set_character_set('utf8mb4')
	data = collateStreamData()
	for item in data:
		text = item['text']
		sentiment_raw = scoreSentiment(text)
		sentiment_linear = scoreSentiment(text, 'linear')
		sentiment_quad = scoreSentiment(text, 'quad')
		sentiment_exp = scoreSentiment(text, 'exp')
		emotions = extractEmotion(text)
		if emotions:
			s = ','
			e_str = s.join(emotions)
		else:
			e_str = ''
		try:
			with closing(db.cursor()) as cursor:
				cursor.execute('SET NAMES utf8mb4;')
				cursor.execute('SET CHARACTER SET utf8mb4;')
				cursor.execute('SET character_set_connection=utf8mb4;')
				cursor.execute("INSERT INTO tweets (text, city, country, sentiment_raw, sentiment_linear, sentiment_quad, sentiment_exp, emotions)\
				VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",\
				(item['text'], item['city'], item['country'], sentiment_raw, sentiment_linear, sentiment_quad, sentiment_exp, e_str))
			db.commit()
		except:
			db.rollback()
			print 'Failed SQL query'
	db.close()
	unlinkStreamData()
