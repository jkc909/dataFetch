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

	def test_retId(self):
		retId = Spider(self.page).retId
		print('retId:',retId)
		self.assertTrue(type(retId) is int)

	def test_URL(self):
		url = Spider(self.page).createUrl()
		print('URL:',url)
		self.assertTrue(type(url) is str)

	def test_crawlTime(self):
		time = Spider(self.page).crawlTime()
		print('CrawlTime:',time)
		self.assertTrue(type(time) is datetime)
		
	def test_findbreadcrumb(self):
		breadcrumb = Spider(self.page).findbreadcrumb()
		print('Breadcrumb:',breadcrumb)
		self.assertTrue(type(breadcrumb) is str)
		self.assertTrue(len(breadcrumb) < 255)
		
	def test_findProductName(self):
		product_name = Spider(self.page).findProductName()
		self.assertTrue(type(product_name) is str)
		self.assertTrue(len(product_name) < 255)
		print('Product Name:',product_name)

	def test_findAnsweredQuestions(self):
		answered_questions = Spider(self.page).findAnsweredQuestions()
		print('Answered Questions:',answered_questions)
		self.assertTrue(type(answered_questions) is str or answered_questions==0)

	def test_findImageCount(self):
		image_count = Spider(self.page).findImageCount()
		print('Image Count:',image_count)
		self.assertTrue(type(image_count) is int or type(image_count) is str )

	def test_findMainImage(self):
		main_image = Spider(self.page).findMainImage()
		print('Main Image:',main_image)
		self.assertTrue(type(main_image) is str)
		self.assertTrue(len(main_image) < 255)

	def test_findBuyBoxPrice(self):
		buybox_price = Spider(self.page).findBuyBoxPrice()
		print('BuyBox Price:',buybox_price)
		self.assertTrue(type(buybox_price) is str or type(buybox_price) is float)

	def test_findAplusContent(self):
		aplus_content = Spider(self.page).findAplusContent()
		print('APlus Content:',aplus_content)
		self.assertTrue(type(aplus_content) is bool)

	def test_findShippingPrice(self):
		shipping_price = Spider(self.page).findShippingPrice()
		print('Shipping Price:',shipping_price)
		self.assertTrue(type(shipping_price) is str or shipping_price==0)

	def test_findStockStatus(self):
		stock_status = Spider(self.page).findStockStatus()
		print('Stock Status:',stock_status)
		self.assertTrue(type(stock_status) is bool or type(stock_status) is str)

	def test_findSeller(self):
		seller = Spider(self.page).findSeller()
		print('Seller:',seller)
		self.assertTrue(type(seller) is str)
		self.assertTrue(len(seller) < 255)

	def test_findShippedBy(self):
		shipped_by = Spider(self.page).findShippedBy()
		print('Shipped By:',shipped_by)
		self.assertTrue(type(shipped_by) is str)
		self.assertTrue(len(shipped_by) < 255)

	def test_findDescription(self):
		description = Spider(self.page).findDescription()
		print('Description:',description[0:50],"...")
		self.assertTrue(type(description) is str)
		# self.assertTrue(len(description) < 255)

	def test_findParentASIN(self):
		parent_asin = Spider(self.page).findParentASIN()
		print('Parent Identifier:',parent_asin)
		self.assertTrue(type(parent_asin) is str)
		self.assertTrue(len(parent_asin) < 255)

	def test_findChildASIN(self):
		child_asin = Spider(self.page).findChildASIN()
		print('Child Identifier:',child_asin)
		self.assertTrue(type(child_asin) is str)
		# self.assertTrue(len(child_asin) < 255)

	def test_findRating(self):
		rating = Spider(self.page).findRating()
		print('Rating:',rating)
		self.assertTrue(type(rating) is str)
		self.assertTrue(len(rating) < 255)

	def test_findReviewCount(self):
		review_count = Spider(self.page).findReviewCount()
		print('Review Count:',review_count)
		self.assertTrue(type(review_count) is str)
		self.assertTrue(len(review_count) < 255)

	def test_findShippingWeight(self):
		ship_weight = Spider(self.page).findShippingWeight()
		print('Shipping Weight:',ship_weight)
		self.assertTrue(type(ship_weight) is dict)
		self.assertTrue(type(ship_weight['shipping_weight']) is str)
		self.assertTrue(type(ship_weight['shipping_weight_unit']) is str)
		self.assertTrue(len(ship_weight['shipping_weight']) < 255)
		self.assertTrue(len(ship_weight['shipping_weight_unit']) < 255)

	def test_findBestSellers(self):
		best_sellers = Spider(self.page).findBestSellers()
		print('Best Seller1:',best_sellers['best_seller_1'])
		print('Best Seller2:',best_sellers['best_seller_2'])
		print('Best Seller3:',best_sellers['best_seller_3'])
		self.assertTrue(type(best_sellers) is dict)

		self.assertTrue(len(best_sellers['best_seller_1']) < 255)
		self.assertTrue(len(best_sellers['best_seller_2']) < 255)
		self.assertTrue(len(best_sellers['best_seller_3']) <255) 

	def test_findFirstAvailable(self):
		first_available = Spider(self.page).findFirstAvailable()
		print('First Available:',first_available)
		# self.assertTrue(type(first_available) is datetime.date or type(first_available) is str )
		# self.assertTrue(len(first_available) < 255)
		
	def test_findAllTechDetails(self):
		all_tech_details = Spider(self.page).findAllTechDetails()
		print('Tech Details Dic:',all_tech_details)
		self.assertTrue(type(all_tech_details) is dict or type(all_tech_details) is str )
		self.assertTrue(len(all_tech_details) < 255)
		
	def test_findBrandName(self):
		brand_name = Spider(self.page).findBrandName()
		print('Brand Name:',brand_name)
		self.assertTrue(type(brand_name) is str)
		self.assertTrue(len(brand_name) < 255)

	def test_findModelNumber(self):
		model_number = Spider(self.page).findModelNumber()
		print('Model Number:',model_number)
		self.assertTrue(type(model_number) is str)
		self.assertTrue(len(model_number) < 255)

	def test_findItemWeight(self):
		item_weight = Spider(self.page).findItemWeight()
		print('Item Weight:',item_weight['weight'])
		print('Item Weight Unit:',item_weight['weight_unit'])
		self.assertTrue(type(item_weight) is dict)
		self.assertTrue(len(item_weight) < 255)

	def test_findDimensions(self):
		dimensions = Spider(self.page).findDimensions()
		print('Dimensions:',dimensions)
		self.assertTrue(type(dimensions) is dict)
		self.assertTrue(len(dimensions) < 255)

	def test_findStockMessage(self):
		stock_message = Spider(self.page).findStockMessage()
		print('Stock Message:',stock_message)
		self.assertTrue(type(stock_message) is str)
		self.assertTrue(len(stock_message) < 255)

	def test_findZipCode(self):
		zipcode = Spider(self.page).findZipCode()
		print('ZipCode:',zipcode)
		self.assertTrue(type(zipcode) is str)
		self.assertTrue(len(zipcode) < 255)




if __name__ == '__main__':
	path = 'amazonfiles/'
	files = []
	for file in os.listdir(path):
		if file == '.DS_Store':
			continue
		ok = str(path+file)
		files.append(ok)
	unittest.main()
	 