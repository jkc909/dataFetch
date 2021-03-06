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
        while True:
            try:
                breadcrumb = self.content.find("div",attrs={'id':"wayfinding-breadcrumbs_feature_div"})
                if breadcrumb:
                    break
            except:
                pass
            breadcrumb = '[!Error: breadcrumb Not Found]'
            return breadcrumb
        try:
            breadcrumb = ' '.join(''.join(breadcrumb.text).split()).replace("›","|")
        except:
            breadcrumb = '[!Error: breadcrumb Could Not Parse]'
        return breadcrumb

    def findProductName(self):
        while True:
            try:
                product_name = self.content.find('span',attrs={'id':'productTitle'})
                if product_name:
                    break
            except:
                pass
            product_name = '[!Error: product_name Not Found]'
            return product_name
        try: 
            product_name = ' '.join(''.join(product_name).split())
        except:   
            product_name = '[!Error: product_name Could Not Parse]'
        return product_name

    def findAnsweredQuestions(self):  
        while True:
            try:
                ans_quest = self.content.find('a',attrs={'id','askATFLink'}).span
                if ans_quest:
                    break
            except:
                pass
            ans_quest = 0
            return ans_quest
        try:
             ans_quest = ' '.join(''.join(ans_quest.text.replace('answered questions','')).split())
        except:
            ans_quest = '[!Error: ans_quest Could Not Parse]'
        return ans_quest

    def findImageCount(self):
        while True:
            try:
                image_count =    len(self.content.find('div',attrs={'id':'altImages'}).find('ul').findAll('li', class_='a-spacing-small item'))
                if image_count:
                    return image_count
            except:
                pass
            try:
                image_count =    len(self.content.find('div',attrs={'id':'altImages'}).find('ul').findAll('li', class_='a-spacing-small item imageThumbnail a-declarative'))
                if image_count:
                    return image_count
            except:
                pass
            image_count = '[!Error: image_count Not Found]'
            return image_count
        return image_count

    def findMainImage(self):
        while True:
            try:
                main_image = self.content.find('span', attrs={'data-action':'main-image-click'}).div.img['src']
                if main_image:
                    if main_image is None or len(main_image) > 100:
                        try:
                            main_image = self.content.find('span', attrs={'data-action':'main-image-click'}).div.img['data-old-hires']
                            if main_image:
                                break
                        except:
                            main_image = '[!Error: main_image Not Found]'
                            return main_image
            except:
                pass
            # print(main_image)

            main_image = '[!Error: main_image Not Found]'
            return main_image
        try:
            main_image = ' '.join(''.join(main_image).split())
        except:
            main_image = '[!Error: main_image Could Not Parse]'
        return main_image

    def findBuyBoxPrice(self):
        while True:
            try:
                buybox_price = float(self.content.find('div',attrs={'id':'priceInsideBuyBox_feature_div'}).text.replace('$',''))
                if buybox_price:
                    break
            except:
                pass
            try:
                buybox_price = float(self.content.find('span',attrs={'id':'newBuyBoxPrice'}).text.replace('$',''))
                if buybox_price:
                    break
            except:
                pass
            try:
                buybox_price = float(self.content.find('span',attrs={'class':'a-color-price price3P'}).text.replace('$',''))
                if buybox_price:
                    break
            except:
                pass
            buybox_price = 0
            return buybox_price
        return buybox_price
        
    def findAplusContent(self):
        while True:
            try:
                aplus_content = self.content.find('div',attrs={'id':'aplus'}).text
                if aplus_content:
                    aplus_content = True
                    break
            except:
                pass
            aplus_content = False
            return aplus_content
            break
        return aplus_content

    def findShippingPrice(self):
        while True:
            try:
                shipping_price = self.content.find('span',attrs={'id':'price-shipping-message'}).text
                if shipping_price:
                    break
            except:
                pass
            try:
                shipping_price = self.content.find('span',attrs={'id':'ourprice_shippingmessage'}).text
                if shipping_price:
                    break
            except:
                pass
            shipping_price = 0
            return shipping_price
        if "FREE Shipping" in shipping_price:
            shipping_price = 0
            return shipping_price
        else: 
            try:
                shipping_price = ' '.join(''.join(shipping_price).split())
                shipping_price = re.findall("\d+\.\d+", shipping_price)
                shipping_price = shipping_price[0]

            except:
                shipping_price = 0
        return shipping_price

    def findStockStatus(self):
        while True:
            try:
                stock_status = self.content.find('div',attrs={'id':'availability'}).text
                if stock_status:
                    break
            except:
                pass
            stock_status = '[!Error: stock_status Not Found]'
            return stock_status
        try:
            stock_status = ' '.join(''.join(stock_status).split())
            # print(stock_status)
            if stock_status == 'In Stock.':
                stock_status = True
                return stock_status
            else:
                stock_status = False
                return stock_status
        except:
            stock_status = '[!Error: stock_status Could Not Parse]'
        return stock_status
            
    def findSeller(self):
        while True:
            try:
                seller = self.content.find('div',attrs={'id':'merchant-info'}).select_one('a[href*=seller]')
                if seller:
                    break
            except:
                pass
            try:
                seller = self.content.find('div',attrs={'id':'merchant-info'}).text
                if seller:
                    break
            except:
                pass
            try:
                seller = self.content.find('div',attrs={'id':'shipsFromSoldByInsideBuyBox_feature_div'}).text
                if seller:
                    break
            except:
                pass
            seller = '[!Error: seller Not Found]'
            return seller
        if seller is None:
            seller = '[!Error: seller Could Not Parse]'
        elif "Ships from and sold by Amazon.com" in seller:
            seller= 'Amazon.com'        
        else:
            try:
                seller = seller = ' '.join(''.join(seller.text).split())
            except:
                seller = '[!Error: seller Could Not Parse]'
        return seller

    def findShippedBy(self):
        while True:
            try:
                shipped_by = self.content.find('div',attrs={'id':'merchant-info'}).select_one('a[href*=fulfillment]')
                if shipped_by:
                    break
            except:
                pass
            try:
                shipped_by = self.content.find('div',attrs={'id':'merchant-info'}).text
                if shipped_by:
                    break
            except:
                pass
            shipped_by = '[!Error: shipped_by Not Found]'
            return shipped_by
        else:
            try:
                shipped_by = ' '.join(''.join(shipped_by.text).split())
            except:
                shipped_by = '[!Error: Could Not Parse]'
        if 'Fulfilled by Amazon' in shipped_by:
            shipped_by = 'Amazon.com'
        elif 'Ships from and sold by Amazon.com' in shipped_by: 
            shipped_by = 'Amazon.com'
        elif 'Ships from and sold by' in shipped_by:
            try:
                shipped_by = self.content.find('div',attrs={'id':'merchant-info'}).select_one('a[href*=merchant_link]').text
                shipped_by = ' '.join(''.join(shipped_by.text).split())
            except:
                shipped_by = '[!Error: shipped_by Not Found]'
        return shipped_by    

    def findDescription(self):
        return("need to fix this")
        # while True:
        #     try:
        #         description = self.content.find('div',attrs={'id':'aplus_feature_div'}).text
        #         # print(description)
        #         # description = re.sub(r'[^*]*\}*\)*\;*\}(.*)',r'\1',description)
        #         description = ' '.join(''.join(description).split())
        #         description = re.sub(r'[^*]*\}*\)*\;*\}(.*)',r'\1',description)
        #         description = re.sub(r'[^*]*emoving for for carousel, reinvestigate(.*)',r'\1',description)
        #         description = ' '.join(''.join(description).split())
        #         return description
        #     except:
        #         pass
        #     try:
        #         description = re.sub(r'.*\#productDescription[^*]*','',(self.content.find('div',attrs={'id':'productDescription_feature_div'})).text).replace('Product description','')
        #         if description:
        #             description = ' '.join(''.join(description).split())
        #             return description
        #     except:
        #         pass
        #     try:
        #         description = re.sub(r'[^*]*\}*\)*\;*\}','',(self.content.find('div',attrs={'id':'aplus3p_feature_div'})).text)
        #         if description:
        #             description = ' '.join(''.join(description).split())
        #             return description
        #     except:
        #         pass


        #     description = '[!Error: description Not Found]'
        #     return description
        # return description

    def findParentASIN(self):
        while True:
            try:
                parent_asin = re.sub(r'.*parentAsin":"(.*?)(",").*',r'\1',self.content.find('script',attrs={'type':'a-state'},text=re.compile(r'.*parentAsin.*')).text)
                if parent_asin:
                    break
            except:
                pass

            try:
                
                parent_asin = self.content.find('div',attrs={'id':'tell-a-friend'})['data-dest']
                # import code; code.interact(local=dict(globals(), **locals())) 
                parent_asin = re.sub(r'.*&parentASIN=(.*?)(&.*).*',r'\1',parent_asin)


                if parent_asin:
                    break
            except:
                pass

            parent_asin = '[!Error: parent_asin Not Found]'
            return parent_asin
        return parent_asin


    def findProductDetails(self):
        while True:
            try:
                PRODUCT_DETAILS = self.content.find('table',attrs={"id":"productDetails_detailBullets_sections1"})
                if PRODUCT_DETAILS:
                    break
            except:
                pass

            try:
                PRODUCT_DETAILS = self.content.find('div',attrs={"id":"detail-bullets"})
                if PRODUCT_DETAILS:
                    break
            except:
                pass

            PRODUCT_DETAILS = '[!Error: PRODUCT_DETAILS Not Found]'
            return PRODUCT_DETAILS
        return PRODUCT_DETAILS

    def findChildASIN(self):
        while True:
            try:
                child_asin = self.PRODUCT_DETAILS.find('th',text=re.compile(r'.*ASIN.*')).findNext('td').contents[0]
                if child_asin:
                    break
            except:
                pass

            try: 
                child_asin = self.PRODUCT_DETAILS.find('b',text=re.compile('.*ASIN:.*')).find_parent().text
                child_asin = re.sub("ASIN: ","",child_asin)
                if child_asin:
                    break
            except:
                pass
            child_asin = False
            return child_asin
        try:
            child_asin = ' '.join(''.join(child_asin).split())
        except:
            child_asin = False
        return child_asin
        
    def findRating(self):
        while True:
            try:
                rating = self.PRODUCT_DETAILS.find('th',text=re.compile(r'.*Customer Reviews.*')).findNext('td').text
                if rating:
                    break
            except:
                pass
            rating = None
            return rating
        try:
            rating = re.sub("out of.*","",re.search(r".*out of.*",rating).group(0)).replace(" ","")
        except:
            rating = None
        return rating

    def findReviewCount(self):
        while True:
            try:
                review_count = self.PRODUCT_DETAILS.find('th',text=re.compile(r'.*Customer Reviews.*')).findNext('td').text
                if review_count:
                    break
            except:
                pass
            review_count = '[!Error: review_count Not Found]'
            break
        if 'Be the first to review this item' in review_count:
            review_count = 0
            return review_count
        try:
            review_count = re.sub("customer reviews.*","",re.search(r".*\d customer reviews.*",review_count).group(0)).replace(" ","").replace(',','')
        except:
            pass
        try:
            review_count = re.sub("customer review.*","",re.search(r".*\d customer review.*",review_count).group(0)).replace(" ","").replace(',','')
        except:
            pass
        return review_count

    def findShippingWeight(self):
        while True:
            try:
                RAW_SHIPPING_WEIGHT = self.PRODUCT_DETAILS.find('th',text=re.compile(r'.*Shipping Weight.*')).findNext('td').text
                if RAW_SHIPPING_WEIGHT:
                    break
            except:
                pass
            RAW_SHIPPING_WEIGHT = 0
            break
        try:
            shipping_weight = re.sub(r"(\d) .*",r"\1",RAW_SHIPPING_WEIGHT)
            shipping_weight = ' '.join(''.join(shipping_weight.split())).replace(" ","")
        except:
            shipping_weight = 0
        try:
            shipping_weight_unit = re.sub(r".*\d (.*) \(.*",r"\1",RAW_SHIPPING_WEIGHT)
            shipping_weight_unit = ' '.join(''.join(shipping_weight_unit.split())).replace(" ","")
        except:
            shipping_weight_unit = '[!Error: shipping_weight_unit Could Not Parse]'
        SHIPWEIGHT = dict();
        SHIPWEIGHT['shipping_weight'] = shipping_weight
        SHIPWEIGHT['shipping_weight_unit'] = shipping_weight_unit
        return SHIPWEIGHT

    def findBestSellers(self):
        while True:
            try:
                RAW_BEST_SELLER = self.PRODUCT_DETAILS.find('th',text=re.compile(r'.*Best Sellers Rank.*')).findNext('td')
                BEST_SELLER_PARSE = RAW_BEST_SELLER.findAll('span')
                if RAW_BEST_SELLER:
                    break
            except:
                pass

            try: 
                # import code; code.interact(local=dict(globals(), **locals()))
                RAW_BEST_SELLER = self.PRODUCT_DETAILS.find('b',text=re.compile('.*ASIN:.*')).find_parent().text
                child_asin = re.sub("ASIN: ","",child_asin)
                if child_asin:
                    break
            except:
                pass

            RAW_BEST_SELLER = '[!Error: BESTSELLERS Not Found]'
            break 
        try:
            best_seller_1 = ' '.join(''.join(BEST_SELLER_PARSE[1].text).split()).replace(">","|")
        except:
            best_seller_1 = '[!Error: Not Found]'
        try:
            best_seller_2 = ' '.join(''.join(BEST_SELLER_PARSE[2].text).split()).replace(">","|")
        except IndexError:
            best_seller_2 = ''
        except:
            best_seller_2 = '[!Error: Not Found]'
        try:
            best_seller_3 = ' '.join(''.join(BEST_SELLER_PARSE[3].text).split()).replace(">","|")
        except IndexError:
            best_seller_3 = ''
        except:
            best_seller_3 = '[!Error: Not Found]'
        BESTSELLERS = dict();
        BESTSELLERS['best_seller_1'] = best_seller_1
        BESTSELLERS['best_seller_2'] = best_seller_2
        BESTSELLERS['best_seller_3'] = best_seller_3
        return BESTSELLERS

    def findFirstAvailable(self):
        while True:
            try:
                first_available = self.PRODUCT_DETAILS.find('th',text=re.compile(r'.*Date First Available.*')).findNext('td').text
                if first_available:
                    break
            except:
                pass
            try:
                first_available = self.PRODUCT_DETAILS.find('th',text=re.compile(r'.*Date first listed on Amazon.*')).findNext('td').text
                if first_available:
                    break
            except:
                pass
            first_available = '2011-09-09 00:00:00'
            return first_available
        try:
            first_available = ' '.join(''.join(first_available).split())
            first_available = datetime.strptime(first_available, '%B %d, %Y').date()
        except:
            first_available = '[!Error: first_available Could Not Parse]'
        return first_available

    def findTechnicalDetailsBlock(self):
        while True:
            try:
                TECHNICAL_DETAILS =    self.content.find('div',attrs={"id":"prodDetails"})
                if TECHNICAL_DETAILS:
                    break
            except:
                pass
            try:
                TECHNICAL_DETAILS =    self.content.find('div',attrs={"id":"productDetails_feature_div"})
                if TECHNICAL_DETAILS:
                    break
            except:
                pass        
            TECHNICAL_DETAILS = '[!Error: TECHNICAL_DETAILS Not Found]'
            return TECHNICAL_DETAILS
        return TECHNICAL_DETAILS

    def findAllTechDetails(self):
        TECH_DETAILS_DICT = {}   
        while True:
            try:
                DETAILS = self.TECHNICAL_DETAILS.find('table',attrs={'id':'productDetails_techSpec_section_1'}).find_all('tr')
                if DETAILS:
                    break
            except:
                pass
            TECH_DETAILS_DICT = '[!Error: TECH_DETAILS_DICT Not Found]'
            return TECH_DETAILS_DICT
        try:
            for i in DETAILS:
                col1 = ' '.join(''.join(i.find('th').text).split())
                col2 = ' '.join(''.join(i.find('td').text).split())
                TECH_DETAILS_DICT.update({col1:col2})
        except:
            TECH_DETAILS_DICT = '[!Error: TECH_DETAILS_DICT Could Not Parse]'
        return TECH_DETAILS_DICT
            
    def findMoreDetails(self):
        while True:
            try:
                MORE_DETAILS = self.TECHNICAL_DETAILS.find('table',attrs={'id':'productDetails_techSpec_section_1'})
                if MORE_DETAILS:
                    break
            except:
                pass
            try:
                MORE_DETAILS = self.TECHNICAL_DETAILS.find('table',attrs={'id':'productDetails_detailBullets_sections1'})
                if MORE_DETAILS:
                    break
            except:
                pass
            MORE_DETAILS = '[!Error: MORE_DETAILS Not Found]'
            return MORE_DETAILS
        return MORE_DETAILS

    def findBrandName(self):
        while True:
            try:
                brand = self.MORE_DETAILS.find('th',text=re.compile(r'.*brand Name.*')).findNext('td').contents[0]
                if brand:
                    break
            except:
                pass
            try:
                brand =  self.content.find('a',attrs={'id':'bylineInfo'}).text
                if brand:
                    break
            except:
                pass
            brand = '[!Error: brand Not Found]'
            return brand
        try:
            brand = ' '.join(''.join(brand).split())
        except:
            brand = '[!Error: brand Could Not Parse]'
        return brand

    def findModelNumber(self):
        while True:
            try:
                part_number = self.MORE_DETAILS.find('th',text=re.compile(r'.*Item model number.*',re.I)).findNext('td').contents[0]
                if part_number:
                    break
            except:
                pass

            try:
                part_number = self.TECHNICAL_DETAILS.find('th',text=re.compile(r'.*Item model number.*',re.I)).findNext('td').contents[0]
                if part_number:
                    break
            except:
                pass

            try:  
                part_number = self.PRODUCT_DETAILS.find('b',text=re.compile('.*Item model number:.*')).find_parent().text
                part_number = re.sub("Item model number: ","",part_number)
                if part_number:
                    break
            except:
                pass 
      
            part_number = '[!Error: part_number Not Found]'
            return part_number
        try:
            part_number = ' '.join(''.join(part_number).split())
        except:
            part_number = '[!Error: part_number Could Not Parse]'
        return part_number

    def findItemWeight(self):
        while True:
            try:
                RAW_ITEM_WEIGHT = self.MORE_DETAILS.find('th',text=re.compile(r'.*Item Weight.*')).findNext('td').contents[0]
            except:
                pass
            try:
                RAW_ITEM_WEIGHT = self.TECHNICAL_DETAILS.find('th',text=re.compile(r'.*Item Weight.*')).findNext('td').contents[0]
            except:
                pass 
            break
        try:
            product_weight = re.sub(r"(\d) .*",r"\1",RAW_ITEM_WEIGHT)
            product_weight = ' '.join(''.join(product_weight.split())).replace(" ","")
        except:
            product_weight = 0



            # return product_weight
        try:
           product_weight_unit = re.sub(r".*\d (.*)",r"\1",RAW_ITEM_WEIGHT)
           product_weight_unit = ' '.join(''.join(product_weight_unit.split())).replace(" ","")
        except:
           product_weight_unit = '[!Error: product_weight_unit Not Found]'
           # return product_weight
        ITEMWEIGHT = dict();
        ITEMWEIGHT['weight'] = product_weight
        ITEMWEIGHT['weight_unit'] = product_weight_unit
        return ITEMWEIGHT

    def findDimensions(self):
        while True:
            try:
                dimensions = ' '.join(''.join(self.MORE_DETAILS.find('th',text=re.compile(r'.*Product Dimensions.*',re.I)).findNext('td').contents[0]).split())
                if dimensions:
                    break
            except:
                pass
            try:
                dimensions = ' '.join(''.join(self.TECHNICAL_DETAILS.find('th',text=re.compile(r'.*Product dimensions.*',re.I)).findNext('td').contents[0]).split())
                if dimensions:
                    break
            except:
                pass      
            break
        try:
            dimensions_unit = ' '.join(''.join(re.sub('.*\d','',dimensions.split('x')[2])).split())
        except:
            dimensions_unit = '[!Error: dimensions_unit Not Found]'
            
        try:
            dimensions = dimensions.replace(dimensions_unit,'').replace(' ','').split('x')
        except:
            dimensions = {}
        DIMS = dict();
        DIMS['dimensions'] = str(json.dumps(dimensions))
        DIMS['dimensions_unit'] = dimensions_unit
        return DIMS

    def findStockMessage(self):
        while True:
            try:
                stock_message = self.content.find('div',attrs={'id':'availability'}).text
                if stock_message:
                    break
            except:
                pass
            stock_message = ''
            return stock_message
        if "left in stock" in stock_message:
            try:
                stock_message =' '.join(''.join(re.sub(r".*(Only)",r"\1",stock_message)).split())
                return stock_message
            except:
                stock_message = '[!Error: stock_message Could Not Parse]'
        try:
            stock_message = ' '.join(''.join(stock_message).split())
            return stock_message
        except:
            stock_message = '[!Error: stock_message Could Not Parse]'
        return stock_message

    def findZipCode(self):
        while True:
            try:
                zip_code = self.content.find('div',attrs={'id':'contextualIngressPtLabel_deliveryShortLine'}).text
                if zip_code:
                    break
            except:
                pass
            zip_code = '[!Error: zip_code Not Found]'
            return zip_code
        try:
            zip_code = ' '.join(''.join(re.sub(r".* ",r"",zip_code)).split())
        except:
            zip_code = '[!Error: zip_code Could Not Parse]'
        return str(zip_code.encode('ascii', 'ignore').decode("utf-8"))
