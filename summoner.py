class Data:
    def __init__(self, html, retId = 0):
        self.content = html
        self.retId = retId
        if self.retId == 1:
            from amz_parser import Spider
            self.SpiderInstance = Spider(self.content)
        elif self.retId == 2:
            from retailer2 import ret_2_pdp_parser 
            self.SpiderInstance = ret_2_pdp_parser.Spider(self.content)
            
    def payload(self):
        payload=(Data.crawl_data(self),\
                Data.technical_details(self),
                self.staChildIdentifier)
        print(payload)
        return payload

    def technical_details(self):
        TECH_DETAILS_DICT = {}
        try:
            TECH_DETAILS_DICT = self.SpiderInstance.findAllTechDetails()
        except:
            pass
        return TECH_DETAILS_DICT

    def crawl_data(self):
        self.staChildIdentifier = self.SpiderInstance.findChildASIN()

        data = {}
        try:
            data['staRetId'] = self.SpiderInstance.retId
        except:
            pass
        try:
            data['staProductName'] = self.SpiderInstance.findProductName()
        except:
            pass
        try:
            data['staBreadcrumb'] = self.SpiderInstance.findbreadcrumb()
        except:
            pass
        try:
            data['staOptionName'] = 'Need to add this'
        except:
            pass
        try:
            data['staChildIdentifier'] = self.SpiderInstance.findChildASIN()
        except:
            pass
        try:
            data['staUrl'] = self.SpiderInstance.createUrl()
        except:
            pass
        try:
            data['staParentIdentifier'] = self.SpiderInstance.findParentASIN()
        except:
            pass
        try:
            data['staPartNumber'] = self.SpiderInstance.findModelNumber()
        except:
            pass
        try:
            data['staImageCount'] = self.SpiderInstance.findImageCount()
        except:
            pass
        try:
            data['staDescription'] = self.SpiderInstance.findDescription()
        except:
            pass
        try:
            data['staMainImage'] = self.SpiderInstance.findMainImage()
        except:
            pass
        try:
            data['staShippingWeight'] = self.SpiderInstance.findShippingWeight()['shipping_weight']
        except:
            pass
        try:
            data['staShippingWeightUnit'] = self.SpiderInstance.findShippingWeight()['shipping_weight_unit']
        except:
            pass
        try:
            data['staBestSeller1'] = self.SpiderInstance.findBestSellers()['best_seller_1']
        except:
            pass
        try:
            data['staBestSeller2'] = self.SpiderInstance.findBestSellers()['best_seller_2']
        except:
            pass
        try:
            data['staBestSeller3'] = self.SpiderInstance.findBestSellers()['best_seller_3']
        except:
            pass
        try:
            data['staFirstAvailable'] = self.SpiderInstance.findFirstAvailable()
        except:
            pass
        try:
            data['staBrand'] = self.SpiderInstance.findBrandName()
        except:
            pass
        try:
            data['staItemWeight'] = self.SpiderInstance.findItemWeight()['weight']
        except:
            pass
        try:
            data['staItemWeightUnit'] = self.SpiderInstance.findItemWeight()['weight_unit']
        except:
            pass
        try:
            data['staDimensions'] = self.SpiderInstance.findDimensions()['dimensions']
        except:
            pass
        try:
            data['staDimensionsUnit'] = self.SpiderInstance.findDimensions()['dimensions_unit']
        except:
            pass
        try:
            data['staAplus'] = self.SpiderInstance.findAplusContent()
        except:
            pass

        # DYNAMIC DATA
        try:
            data['dynPrice'] = self.SpiderInstance.findBuyBoxPrice()
        except:
            pass
        try:
            data['dynStockStatus'] = self.SpiderInstance.findStockStatus()
        except:
            pass
        try:
            data['dynSeller'] = self.SpiderInstance.findSeller()
        except:
            pass
        try:
            data['dynShippedBy'] = self.SpiderInstance.findShippedBy()
        except:
            pass
        try:
            data['dynShipPrice'] = self.SpiderInstance.findShippingPrice()
        except:
            pass
        try:
            data['dynAnsweredQuestions'] = self.SpiderInstance.findAnsweredQuestions()
        except:
            pass
        try:
            data['dynRating'] = self.SpiderInstance.findRating()
        except:
            pass
        try:
            data['dynReviewCount'] = self.SpiderInstance.findReviewCount()
        except:
            pass
        try:
            data['dynStockMessage'] = self.SpiderInstance.findStockMessage()
        except:
            pass
        try:
            data['dynZipCode'] = self.SpiderInstance.findZipCode()
        except:
            pass
        try:
            data['dynCrawlTime'] = self.SpiderInstance.crawlTime()
        except:
            pass
        return data
