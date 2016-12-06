import tweepy
import json
import time

class StreamListener(tweepy.StreamListener):

	requires_location = True

	def __init__(self, file_to_write, time_limit=60, count_limit=500):
		self.file_to_write = file_to_write
		self.count = 0
		self.start_time = time.time()
		self.limit = time_limit
		self.count_limit = count_limit
		super(StreamListener, self).__init__()

	def extract_data(self, data):
		return {'text': json.loads(data)['text'],
				'created_at': json.loads(data)['created_at'],
				'place': json.loads(data)['place']['full_name'],
				'country': json.loads(data)['place']['country']}

	def on_status(self, status):
		if (time.time() - self.start_time) < self.limit and self.count <= self.count_limit:
			if status.retweeted or (self.requires_location == True and status.place is None):
				return
			else:
				try:
					with open(self.file_to_write, 'a') as f:
						data = json.dumps(status._json)
						extract = self.extract_data(data)
						if self.count == 0:
							prepend = '['
						else:
							prepend = ','
						f.write(prepend + json.dumps(extract))
						self.count += 1
						print self.count
						return True
				except BaseException as e:
					print('Error on_status: %s' % str(e))
				return True
		else:
			end_file = open(self.file_to_write, 'a')
			end_file.write(']')
			end_file.close()
			print 'Closing stream'
			return False

	def on_error(self, status_code):
		if status_code == 420:
			return False

class TrainStreamListener(StreamListener):
# streamer to capture training data for classifiers
	requires_location = False

	def __init__(self, file_to_write, bias, time_limit=60, count_limit=500):
		self.file_to_write = file_to_write
		self.bias = bias
		self.count = 0
		self.start_time = time.time()
		self.limit = time_limit
		self.count_limit = count_limit
		super(StreamListener, self).__init__()

	def extract_data(self, data):
		return {'text': json.loads(data)['text'],
				'label': self.bias}
