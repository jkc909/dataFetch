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

	def test_findProductDetails(self):
		product_details = Spider(self.page).findProductDetails()
		print('Found Product Details:',bool(product_details))

	def test_findTechnicalDetailsBlock(self):
		tech_details = Spider(self.page).findTechnicalDetailsBlock()
		print('Found Technical Details:',bool(tech_details))

	def test_findMoreDetails(self):
		more_details = Spider(self.page).findMoreDetails()
		print('Found More Details:',bool(more_details))
