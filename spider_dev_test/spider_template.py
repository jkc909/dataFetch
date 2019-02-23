
path = 'json_files/'
import os
for file in os.listdir(path):
	print(file)
	if file == '.DS_Store':
		continue
	ok = str(path+file)
	print(ok)
	assert os.path.isfile(path+file)
	with open(ok, "rb") as file:
		page = file.read()
		file.close()
	data = json.loads(page)
	bs_html = BeautifulSoup(page, 'html.parser', from_encoding='utf-8')
	

from bs4 import BeautifulSoup
from datetime import datetime
import re
import json

class Spider:
    """
    List of all parser functions for Amazon

    These functions will ~generally~ follow this logic path:
        - start a loop that will continue indefinitely
        - try to find the tag
            * if the tag finder returns a true value, move on to the parsing
            * if the tag finder returns a false value, try the next tag finder
            * if none of the available tag finders return a true value: return an error message
        - try to parse the information out of the data
        - return either an error message or a formatted data point

    """

    def __init__(self, html):
        self.retId = 1
        self.content = html
        self.PRODUCT_DETAILS = Spider.findProductDetails(self)    
        self.TECHNICAL_DETAILS = Spider.findTechnicalDetailsBlock(self)
        self.MORE_DETAILS = Spider.findMoreDetails(self)

######### Parser functions ########

    def createUrl(self):
    	childid = Spider.findChildASIN(self)
    	page_url = "http://www.amazon.com/dp/"+(''.join(childid))
    	return page_url

    def crawlTime(self):
        DATETIME = datetime.now().replace(microsecond=0)
        return DATETIME

    def findbreadcrumb(self):
        pass

    def findProductName(self):
        pass

    def findAnsweredQuestions(self):  
        pass

    def findImageCount(self):
        pass

    def findMainImage(self):
        pass

    def findBuyBoxPrice(self):
        pass

    def findAplusContent(self):
        pass

    def findShippingPrice(self):
        pass
    def findStockStatus(self):
    	pass
            
    def findSeller(self):
        pass

    def findShippedBy(self):
        pass  

    def findDescription(self):
        pass

    def findParentASIN(self):
        pass

    def findProductDetails(self):
        pass

    def findChildASIN(self):
        pass
        
    def findRating(self):
        pass

    def findReviewCount(self):
        pass

    def findShippingWeight(self):
        pass

    def findBestSellers(self):
        pass

    def findFirstAvailable(self):
        pass

    def findTechnicalDetailsBlock(self):
        pass

    def findAllTechDetails(self):
        pass
            
    def findMoreDetails(self):
        pass

    def findBrandName(self):
        pass

    def findModelNumber(self):
        pass

    def findItemWeight(self):
        pass

    def findDimensions(self):
        pass

    def findStockMessage(self):
        pass

    def findZipCode(self):
    	pass