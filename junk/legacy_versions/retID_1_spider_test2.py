
from bs4 import BeautifulSoup
from datetime import datetime
import re
import json
from amz_parser import Spider




class Data:
    """
    """

    def __init__(self, html):
        """
        """
        self.content = html


    def technical_details(self):
        TECH_DETAILS_DICT = Spider(self.content).findAllTechDetails()
        return TECH_DETAILS_DICT

    def crawl_data(self):
        """
        """
        data = {}
        try:
            data['staRetId'] = Spider(self.content).retId
        except:
            pass
        try:
            data['staProductName'] = Spider(self.content).findProductName()
        except:
            pass
        try:
            data['staBreadcrumb'] = Spider(self.content).findbreadcrumb()
        except:
            pass
        try:
            data['staOptionName'] = 'Need to add this'
        except:
            pass
        try:
            data['staChildIdentifier'] = Spider(self.content).findChildASIN()
        except:
            pass
        try:
            data['staUrl'] = Spider(self.content).createUrl()
        except:
            pass
        try:
            data['staParentIdentifier'] = Spider(self.content).findParentASIN()
        except:
            pass
        try:
            data['staPartNumber'] = Spider(self.content).findModelNumber()
        except:
            pass
        try:
            data['staImageCount'] = Spider(self.content).findImageCount()
        except:
            pass
        try:
            data['staDescription'] = "PASS UNTIL YOU FIX THIS SHEIT"
        except:
            pass
        try:
            data['staMainImage'] = Spider(self.content).findMainImage()
        except:
            pass
        try:
            data['staShippingWeight'] = Spider(self.content).findShippingWeight()['shipping_weight']
        except:
            pass
        try:
            data['staShippingWeightUnit'] = Spider(self.content).findShippingWeight()['shipping_weight_unit']
        except:
            pass
        try:
            data['staBestSeller1'] = Spider(self.content).findBestSellers()['best_seller_1']
        except:
            pass
        try:
            data['staBestSeller2'] = Spider(self.content).findBestSellers()['best_seller_2']
        except:
            pass
        try:
            data['staBestSeller3'] = Spider(self.content).findBestSellers()['best_seller_3']
        except:
            pass
        try:
            data['staFirstAvailable'] = Spider(self.content).findFirstAvailable()
        except:
            pass
        try:
            data['staBrand'] = Spider(self.content).findBrandName()
        except:
            pass
        try:
            data['staItemWeight'] = Spider(self.content).findItemWeight()['weight']
        except:
            pass
        try:
            data['staItemWeightUnit'] = Spider(self.content).findItemWeight()['weight_unit']
        except:
            pass
        try:
            data['staDimensions'] = Spider(self.content).findDimensions()['dimensions']
        except:
            pass
        try:
            data['staDimensionsUnit'] = Spider(self.content).findDimensions()['dimensions_unit']
        except:
            pass
        try:
            data['staAplus'] = Spider(self.content).findAplusContent()
        except:
            pass

        # DYNAMIC DATA
        try:
            data['dynPrice'] = Spider(self.content).findBuyBoxPrice()
        except:
            pass
        try:
            data['dynStockStatus'] = Spider(self.content).findStockStatus()
        except:
            pass
        try:
            data['dynSeller'] = Spider(self.content).findSeller()
        except:
            pass
        try:
            data['dynShippedBy'] = Spider(self.content).findShippedBy()
        except:
            pass
        try:
            data['dynShipPrice'] = Spider(self.content).findShippingPrice()
        except:
            pass
        try:
            data['dynAnsweredQuestions'] = Spider(self.content).findAnsweredQuestions()
        except:
            pass
        try:
            data['dynRating'] = Spider(self.content).findRating()
        except:
            pass
        try:
            data['dynReviewCount'] = Spider(self.content).findReviewCount()
        except:
            pass
        try:
            data['dynStockMessage'] = Spider(self.content).findStockMessage()
        except:
            pass
        try:
            data['dynZipCode'] = Spider(self.content).findZipCode()
        except:
            pass
        try:
            data['dynCrawlTime'] = Spider(self.content).crawlTime()
        except:
            pass
        return data
