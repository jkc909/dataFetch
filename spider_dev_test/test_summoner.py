import unittest
import os
import datetime

from amz_parser import *
from summoner import *

path = 'amazonfiles/'
files = []
for file in os.listdir(path):
	if file == '.DS_Store':
		continue
	ok = str(path+file)
	files.append(ok)

class SpiderTest(unittest.TestCase):

	def setUp(self):
		self.retId = 1
		subject = files[2]
		assert os.path.isfile(subject)
		with open(subject, "rb") as file:
			self.page = BeautifulSoup(file.read(), 'html5lib')
			file.close()
		print("In method", self._testMethodName)
	
	def test_createData(self):
		crawldata = Data(self.page, self.retId).crawl_data()
		print(crawldata)
		self.assertTrue(type(crawldata) is dict)

	def test_createDetailsDict(self):
		details_dict = Data(self.page, self.retId).technical_details()
		print(details_dict)
		self.assertTrue(type(details_dict) is dict or type(details_dict) is str)

	def test_payload(self):
		payload = Data(self.page, self.retId).payload()
		print(payload)
		self.assertTrue(type(payload) is list)
		self.assertTrue(len(payload) == 2)

if __name__ == '__main__':
	path = 'amazonfiles/'
	files = []
	for file in os.listdir(path):
		if file == '.DS_Store':
			continue
		ok = str(path+file)
		files.append(ok)
	unittest.main()
	 