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

    def __init__(self, json_payload):
        self.retId = 2
        self.content = json_payload

######### Parser functions ########

    def crawlTime(self):
        DATETIME = datetime.now().replace(microsecond=0)
        return DATETIME

    def findbreadcrumb(self):
        pass

    def findProductName(self):
        return self.content["productName"]

    def findAnsweredQuestions(self):  
        pass

    def findImageCount(self):
        pass

    def findMainImage(self):
        return self.content["image"]["absolutePath"]

    def findBuyBoxPrice(self):
        return self.content["finalPrice"]

    def findAplusContent(self):
        pass

    def findShippingPrice(self):
    	if self.content["hasFreeShipping"] == 'true':
    		return 0
    	elif self.content["hasFreeShipping"] == 'false':
    		return self.content["hasFreeShipping"]
        

    def findStockStatus(self):
    	return self.content["isInStock"]
            
    def findSeller(self):
        pass

    def findShippedBy(self):
        pass  

    def findDescription(self):
        return self.content["longDescription"]

    def findParentASIN(self):
        return self.content["parentItemid"]

    def findProductDetails(self):
        pass

    def findChildASIN(self):
        return self.content["itemid"]
        
    def findRating(self):
        return self.content["averageStarRating"]

    def findReviewCount(self):
        return self.content["totalReviews"]

    def findShippingWeight(self):
        return {'shipping_weight': '0', 'shipping_weight_unit': 'none'}

    def findBestSellers(self):
        return {'best_seller_1': '', 'best_seller_2': '', 'best_seller_3': ''}

    def findFirstAvailable(self):
        return self.content["goLiveDate"]

    def findTechnicalDetailsBlock(self):
        pass

    def findAllTechDetails(self):
        pass
            
    def findMoreDetails(self):
        pass

    def findBrandName(self):
        return self.content["manufacturer"]["name"]

    def findModelNumber(self):
        return self.content["manufacturerPart"]

    def findItemWeight(self):
        return {'weight': '0', 'weight_unit': 'none'}

    def findDimensions(self):
        return {'dimensions': '0', 'dimensions_unit': 'none'}

    def findStockMessage(self):
        return self.content["stockNotesHeadline"]

    def findZipCode(self):
    	pass
