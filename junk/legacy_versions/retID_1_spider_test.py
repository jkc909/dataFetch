
from bs4 import BeautifulSoup
from datetime import datetime
import re


class Spider:

        def __init__(self, html):
            self.content = BeautifulSoup(html, 'html5lib')
            self.PRODUCT_DETAILS = Spider.findProductDetails(self, self.content)    
            self.TECHNICAL_DETAILS = Spider.findTechnicalDetailsBlock(self, self.content)
            self.MORE_DETAILS = Spider.findMoreDetails(self, self.TECHNICAL_DETAILS)
            
        def data(self):

            TECH_DETAILS_DICT = Spider.findAllTechDetails(self, self.TECHNICAL_DETAILS)
            print(TECH_DETAILS_DICT)

            data = {
               # STATIC DATA    
                'RETAILER_NAME': "Amazon",
                'PRODUCT_NAME': Spider.findProductName(self, self.content),
                'breadcrumb': Spider.findbreadcrumb(self, self.content),
                'CHILD_ASIN': Spider.findChildASIN(self, self.PRODUCT_DETAILS),
                'PARENT_ASIN': Spider.findParentASIN(self, self.content),
                'PART_NUMBER': Spider.findModelNumber(self, self.content, self.TECHNICAL_DETAILS),
               # 'CATEGORY':CATEGORY,
                'IMAGE_COUNT': Spider.findImageCount(self, self.content),
                'DESCRIPTION': Spider.findDescription(self, self.content),
                'MAIN_IMAGE': Spider.findMainImage(self, self.content),
                'SHIPPING_WEIGHT': Spider.findShippingWeight(self, self.PRODUCT_DETAILS)['SHIPPING_WEIGHT'],
                'SHIPPING_WEIGHT_UNIT': Spider.findShippingWeight(self, self.PRODUCT_DETAILS)['SHIPPING_WEIGHT_UNIT'],
                'BEST_SELLER_1': Spider.findBestSellers(self, self.PRODUCT_DETAILS)['BEST_SELLER_1'],
                'BEST_SELLER_2': Spider.findBestSellers(self, self.PRODUCT_DETAILS)['BEST_SELLER_2'],
                'BEST_SELLER_3': Spider.findBestSellers(self, self.PRODUCT_DETAILS)['BEST_SELLER_3'],
                'FIRST_AVAILABLE': Spider.findFirstAvailable(self, self.PRODUCT_DETAILS),
                'BRAND': Spider.findBrandName(self, self.content, self.MORE_DETAILS),
                'ITEM_WEIGHT': Spider.findItemWeight(self, self.MORE_DETAILS, self.TECHNICAL_DETAILS)['PRODUCT_WEIGHT'],
                'ITEM_WEIGHT_UNIT': Spider.findItemWeight(self, self.MORE_DETAILS, self.TECHNICAL_DETAILS)['PRODUCT_WEIGHT_UNIT'],
                'DIMENSIONS': Spider.findDimensions(self, self.MORE_DETAILS, self.TECHNICAL_DETAILS)['DIMENSIONS'],
                'DIMENSIONS_UNIT': Spider.findDimensions(self, self.MORE_DETAILS, self.TECHNICAL_DETAILS)['DIMENSIONS_UNIT'],
                'APLUS_CONTENT': Spider.findAplusContent(self, self.content),
                
                
               # DYNAMIC DATA
                'BUYBOX_PRICE': Spider.findBuyBoxPrice(self, self.content),
                'STOCK_STATUS': Spider.findStockStatus(self, self.content),
                'SELLER': Spider.findSeller(self, self.content),
                'SHIPPED_BY': Spider.findShippedBy(self, self.content),
                'SHIP_PRICE': Spider.findShippingPrice(self, self.content),
                'ANSWERED_QUESTIONS': Spider.findAnsweredQuestions(self, self.content),
                'RATING': Spider.findRating(self, self.PRODUCT_DETAILS),
                'REVIEW_COUNT': Spider.findReviewCount(self, self.PRODUCT_DETAILS),
                'STOCK_MESSAGE': Spider.findStockMessage(self, self.content),
                'ZIP_CODE': Spider.findZipCode(self, self.content),
                'CRAWL_TIME': Spider.crawlTime(self)
                # 'LEAD_TIME': Spider.findLeadTime(self, self.content),
                # 'DELIVERY_DATE': Spider.findDeliveryDate(self, self.content)
                }
            return data

            # print(TECH_DETAILS_DICT)

            # print(data)

            # PRODUCT_DETAILS = Spider.findProductDetails(self, self.content)    
            # TECHNICAL_DETAILS = Spider.findTechnicalDetailsBlock(self, self.content)
            # MORE_DETAILS = Spider.findMoreDetails(self, self.content)
            # DATETIME = Spider.crawlTime(self, self.content)

        def crawlTime(self):
            DATETIME = datetime.now().replace(microsecond=0)
            print(DATETIME)
            return DATETIME

        def findbreadcrumb(self, content):
            
            while True:
                
                try:
                    breadcrumb = content.find("div",attrs={'id':"wayfinding-breadcrumbs_feature_div"})
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

        def findProductName(self, content):
            while True:
                
                try:
                    PRODUCT_NAME = content.find('span',attrs={'id':'productTitle'})
                    if PRODUCT_NAME:
                        break
                except:
                    pass
                
                PRODUCT_NAME = '[!Error: PRODUCT_NAME Not Found]'
                return PRODUCT_NAME
                
            try: 
                PRODUCT_NAME = ' '.join(''.join(PRODUCT_NAME).split())
            except:   
                PRODUCT_NAME = '[!Error: PRODUCT_NAME Could Not Parse]'

            return PRODUCT_NAME

        def findAnsweredQuestions(self, content):  
            while True:

                try:
                    ANS_QUEST = content.find('a',attrs={'id','askATFLink'}).span
                    if ANS_QUEST:
                        break
                except:
                    pass
                
                ANS_QUEST = 0
                return ANS_QUEST
            try:
                 ANS_QUEST = ' '.join(''.join(ANS_QUEST.text.replace('answered questions','')).split())
            except:
                ANS_QUEST = '[!Error: ANS_QUEST Could Not Parse]'

            return ANS_QUEST

        def findImageCount(self, content):

            while True:
                
                try:
                    IMAGE_COUNT =    len(content.find('div',attrs={'id':'altImages'}).find('ul').findAll('li', class_='a-spacing-small item'))
                    if IMAGE_COUNT:
                        return IMAGE_COUNT
                except:
                    pass
                
                try:
                    IMAGE_COUNT =    len(content.find('div',attrs={'id':'altImages'}).find('ul').findAll('li', class_='a-spacing-small item imageThumbnail a-declarative'))
                    if IMAGE_COUNT:
                        return IMAGE_COUNT
                except:
                    pass
                
                
                

            IMAGE_COUNT = '[!Error: IMAGE_COUNT Not Found]'
                    
            return IMAGE_COUNT

        def findMainImage(self, content):
            
            while True:
                
                try:
                    MAIN_IMAGE = content.find('span', attrs={'data-action':'main-image-click'}).div.img['src']
                    if MAIN_IMAGE:
                        break
                except:
                    pass

                if MAIN_IMAGE is None or len(MAIN_IMAGE) > 100:
                        try:
                            MAIN_IMAGE = content.find('span', attrs={'data-action':'main-image-click'}).div.img['data-old-hires']
                            if MAIN_IMAGE:
                                break
                        except:
                            pass

                MAIN_IMAGE = '[!Error: MAIN_IMAGE Not Found]'
                return MAIN_IMAGE
            
            try:
                MAIN_IMAGE = ' '.join(''.join(MAIN_IMAGE).split())
            except:
                MAIN_IMAGE = '[!Error: MAIN_IMAGE Could Not Parse]'
            return MAIN_IMAGE

        def findBuyBoxPrice(self, content):
            
            while True:
                
                try:
                    BUYBOX_PRICE = float(content.find('div',attrs={'id':'priceInsideBuyBox_feature_div'}).text.replace('$',''))
                    if BUYBOX_PRICE:
                        break
                except:
                    pass
                
                try:
                    BUYBOX_PRICE = float(content.find('span',attrs={'id':'newBuyBoxPrice'}).text.replace('$',''))
                    if BUYBOX_PRICE:
                        break
                except:
                    pass
                
                BUYBOX_PRICE = '[!Error: BUYBOX_PRICE Not Found]'
                return BUYBOX_PRICE

            return BUYBOX_PRICE
            
        def findAplusContent(self, content):
            
            while True:
                try:
                    APLUS_CONTENT = content.find('div',attrs={'id':'aplus'}).text
                    if APLUS_CONTENT:
                        APLUS_CONTENT = 1
                        break
                except:
                    pass
                APLUS_CONTENT = 0
                return APLUS_CONTENT
                break
         
            return APLUS_CONTENT

        def findShippingPrice(self, content):
            
            while True:
                
                try:
                    SHIPPING_PRICE = content.find('span',attrs={'id':'price-shipping-message'}).text
                    if SHIPPING_PRICE:
                        break
                except:
                    pass
                
                try:
                    SHIPPING_PRICE = content.find('span',attrs={'id':'ourprice_shippingmessage'}).text
                    if SHIPPING_PRICE:
                        break
                except:
                    pass
                
                SHIPPING_PRICE = '[!Error: SHIPPING_PRICE Not Found]'
                return SHIPPING_PRICE
            
            if "FREE Shipping" in SHIPPING_PRICE:
                SHIPPING_PRICE = 0
                return SHIPPING_PRICE
            else: 
                try:
                    SHIPPING_PRICE = ' '.join(''.join(SHIPPING_PRICE).split())
                except:
                    SHIPPING_PRICE = '[!Error: SHIPPING_PRICE Not Found]'

            return SHIPPING_PRICE

        def findStockStatus(self, content):
         
            while True:
                
                try:
                    STOCK_STATUS = content.find('div',attrs={'id':'availability'}).text
                    if STOCK_STATUS:
                        break
                except:
                    pass
                
                STOCK_STATUS = '[!Error: STOCK_STATUS Not Found]'
                return STOCK_STATUS

            try:
                STOCK_STATUS = ' '.join(''.join(STOCK_STATUS).split())
                # print(STOCK_STATUS)
                if STOCK_STATUS == 'In Stock.':
                    STOCK_STATUS = 1
                    return STOCK_STATUS
                else:
                    STOCK_STATUS = 0
                    return STOCK_STATUS
            except:
                STOCK_STATUS = '[!Error: STOCK_STATUS Could Not Parse]'

            return STOCK_STATUS
                
        def findSeller(self, content):
            
            while True:
                try:
                    SELLER = content.find('div',attrs={'id':'merchant-info'}).select_one('a[href*=seller]')
                    if SELLER:
                        break
                except:
                    pass
                
                try:
                    SELLER = content.find('div',attrs={'id':'merchant-info'}).text
                    if SELLER:
                        break
                except:
                    pass

                try:
                    SELLER = content.find('div',attrs={'id':'shipsFromSoldByInsideBuyBox_feature_div'}).text
                    if SELLER:
                        break
                except:
                    pass
                
                SELLER = '[!Error: SELLER Not Found]'
                return SELLER


            if SELLER is None:
                SELLER = '[!Error: SELLER Could Not Parse]'
            elif "Ships from and sold by Amazon.com" in SELLER:
                SELLER= 'Amazon.com'        
            else:
                try:
                    SELLER = SELLER = ' '.join(''.join(SELLER.text).split())
                except:
                    SELLER = '[!Error: SELLER Could Not Parse]'
            return SELLER

        def findShippedBy(self, content):
            
            while True:
                try:
                    SHIPPED_BY = content.find('div',attrs={'id':'merchant-info'}).select_one('a[href*=fulfillment]')
                    if SHIPPED_BY:
                        break
                except:
                    pass

                try:
                    SHIPPED_BY = content.find('div',attrs={'id':'merchant-info'}).text
                    if SHIPPED_BY:
                        break
                except:
                    pass
                
                SHIPPED_BY = '[!Error: SHIPPED_BY Not Found]'
                return SHIPPED_BY
            


            else:
                try:
                    SHIPPED_BY = ' '.join(''.join(SHIPPED_BY.text).split())
                except:
                    SHIPPED_BY = '[!Error: Could Not Parse]'
                
            if 'Fulfilled by Amazon' in SHIPPED_BY:
                SHIPPED_BY = 'Amazon.com'
            elif 'Ships from and sold by Amazon.com' in SHIPPED_BY: 
                SHIPPED_BY = 'Amazon.com'
            elif 'Ships from and sold by' in SHIPPED_BY:
                try:
                    SHIPPED_BY = content.find('div',attrs={'id':'merchant-info'}).select_one('a[href*=merchant_link]').text
                except:
                    SHIPPED_BY = '[!Error: SHIPPED_BY Not Found]'

            return SHIPPED_BY    



        def findDescription(self, content):
            
            while True:
                try:
                    DESCRIPTION = re.sub(r'[^*]*\}*\)*\;*\}(.*)',r'\1',content.find('div',attrs={'id':'aplus_feature_div'}).text)
                    DESCRIPTION = ' '.join(''.join(DESCRIPTION).split())
                    return DESCRIPTION
                except:
                    pass

                
                try:
                    DESCRIPTION = re.sub(r'.*\#productDescription[^*]*','',(content.find('div',attrs={'id':'productDescription_feature_div'})).text).replace('Product description','')
                    if DESCRIPTION:
                        DESCRIPTION = ' '.join(''.join(DESCRIPTION).split())
                        return DESCRIPTION
                except:
                    pass
                
                try:
                    DESCRIPTION = re.sub(r'[^*]*\}*\)*\;*\}','',(content.find('div',attrs={'id':'aplus3p_feature_div'})).text)
                    if DESCRIPTION:
                        DESCRIPTION = ' '.join(''.join(DESCRIPTION).split())
                        return DESCRIPTION
                except:
                    pass
                
                DESCRIPTION = '[!Error: DESCRIPTION Not Found]'
                break

            return DESCRIPTION



        def findParentASIN(self, content):

            while True:
                try:
                    PARENT_ASIN = re.sub(r'.*parentAsin":"(.*?)(",").*',r'\1',content.find('script',attrs={'type':'a-state'},text=re.compile(r'.*parentAsin.*')).text)
                    if PARENT_ASIN:
                        break
                except:
                    pass
                
                PARENT_ASIN = '[!Error: PARENT_ASIN Not Found]'
                return PARENT_ASIN
            return PARENT_ASIN




        ########## PRDOUCT DETAILS BLOCK #########

        def findProductDetails(self, content):
            
            while True:
                try:
                    PRODUCT_DETAILS =    content.find('table',attrs={"id":"productDetails_detailBullets_sections1"})
                    if PRODUCT_DETAILS:
                        break
                except:
                    pass
                
                PRODUCT_DETAILS = '[!Error: PRODUCT_DETAILS Not Found]'
                print(PRODUCT_DETAILS)
                break
            return PRODUCT_DETAILS



        def findChildASIN(self, PRODUCT_DETAILS):
            
            while True:
                try:
                    CHILD_ASIN = PRODUCT_DETAILS.find('th',text=re.compile(r'.*ASIN.*')).findNext('td').contents[0]
                    if CHILD_ASIN:
                        break
                except:
                    pass
                CHILD_ASIN = '[!Error: CHILD_ASIN Not Found]'
                return CHILD_ASIN
            
            try:
                CHILD_ASIN = ' '.join(''.join(CHILD_ASIN).split())
            except:
                CHILD_ASIN = '[!Error: CHILD_ASIN Could Not Parse]'
            print(CHILD_ASIN)
            return CHILD_ASIN
            


        def findRating(self, PRODUCT_DETAILS):
            
            while True:
                try:
                    RATING = PRODUCT_DETAILS.find('th',text=re.compile(r'.*Customer Reviews.*')).findNext('td').text
                    if RATING:
                        break
                except:
                    pass
                
                RATING = '[!Error: RATING Not Found]'
                return RATING
            
            try:
                RATING = re.sub("out of.*","",re.search(r".*out of.*",RATING).group(0)).replace(" ","")
            except:
                RATING = '[!Error: RATING Could Not Parse]'
        #    print(RATING)
            return RATING



        def findReviewCount(self, PRODUCT_DETAILS):

            while True:
                try:
                    REVIEW_COUNT = PRODUCT_DETAILS.find('th',text=re.compile(r'.*Customer Reviews.*')).findNext('td').text
                    if REVIEW_COUNT:
                        break
                except:
                    pass
                
                REVIEW_COUNT = '[!Error: REVIEW_COUNT Not Found]'
                break
            
            if 'Be the first to review this item' in REVIEW_COUNT:
                REVIEW_COUNT = 0
                return REVIEW_COUNT
            
            try:
                REVIEW_COUNT = re.sub("customer reviews.*","",re.search(r".*\d customer reviews.*",REVIEW_COUNT).group(0)).replace(" ","").replace(',','')
            except:
                REVIEW_COUNT = '[!Error: REVIEW_COUNT Could Not Parse]'
        #    print(REVIEW_COUNT)
            return REVIEW_COUNT



        def findShippingWeight(self, PRODUCT_DETAILS):

            while True:
                try:
                    RAW_SHIPPING_WEIGHT = PRODUCT_DETAILS.find('th',text=re.compile(r'.*Shipping Weight.*')).findNext('td').text
                    if RAW_SHIPPING_WEIGHT:
                        break
                except:
                    pass
                
                RAW_SHIPPING_WEIGHT = '[!Error: SHIPPING_WEIGHT Not Found]'
                break
            
            
            try:
                SHIPPING_WEIGHT = re.sub(r"(\d) .*",r"\1",RAW_SHIPPING_WEIGHT)
                SHIPPING_WEIGHT = ' '.join(''.join(SHIPPING_WEIGHT.split())).replace(" ","")
            except:
                SHIPPING_WEIGHT = '[!Error: SHIPPING_WEIGHT Could Not Parse]'
        #    print(SHIPPING_WEIGHT)


            try:
                SHIPPING_WEIGHT_UNIT = re.sub(r".*\d (.*) \(.*",r"\1",RAW_SHIPPING_WEIGHT)
                SHIPPING_WEIGHT_UNIT = ' '.join(''.join(SHIPPING_WEIGHT_UNIT.split())).replace(" ","")
            except:
                SHIPPING_WEIGHT_UNIT = '[!Error: SHIPPING_WEIGHT_UNIT Could Not Parse]'
        #    print(SHIPPING_WEIGHT_UNIT)

            SHIPWEIGHT = dict();
            SHIPWEIGHT['SHIPPING_WEIGHT'] = SHIPPING_WEIGHT
            SHIPWEIGHT['SHIPPING_WEIGHT_UNIT'] = SHIPPING_WEIGHT_UNIT
            return SHIPWEIGHT



        def findBestSellers(self, PRODUCT_DETAILS):

            while True:
                try:
                    RAW_BEST_SELLER = PRODUCT_DETAILS.find('th',text=re.compile(r'.*Best Sellers Rank.*')).findNext('td')
                    BEST_SELLER_PARSE = RAW_BEST_SELLER.findAll('span')
                    if RAW_BEST_SELLER:
                        break
                except:
                    pass
                
                RAW_BEST_SELLER = '[!Error: BESTSELLERS Not Found]'
                break 
            
            
            try:
                BEST_SELLER_1 = ' '.join(''.join(BEST_SELLER_PARSE[1].text).split()).replace(">","|")
            except:
                BEST_SELLER_1 = '[!Error: Not Found]'
                
        #    print(BEST_SELLER_1)
            try:
                BEST_SELLER_2 = ' '.join(''.join(BEST_SELLER_PARSE[2].text).split()).replace(">","|")
            except IndexError:
                BEST_SELLER_2 = ''
            except:
                BEST_SELLER_2 = '[!Error: Not Found]'
        #    print(BEST_SELLER_2)
            
            try:
                BEST_SELLER_3 = ' '.join(''.join(BEST_SELLER_PARSE[3].text).split()).replace(">","|")
            except IndexError:
                BEST_SELLER_3 = ''
            except:
                BEST_SELLER_3 = '[!Error: Not Found]'
        #    print(BEST_SELLER_2)

            
            BESTSELLERS = dict();
            BESTSELLERS['BEST_SELLER_1'] = BEST_SELLER_1
            BESTSELLERS['BEST_SELLER_2'] = BEST_SELLER_2
            BESTSELLERS['BEST_SELLER_3'] = BEST_SELLER_3
            return BESTSELLERS

          

        def findFirstAvailable(self, PRODUCT_DETAILS):

            while True:
                try:
                    FIRST_AVAILABLE = PRODUCT_DETAILS.find('th',text=re.compile(r'.*Date First Available.*')).findNext('td').text
                    if FIRST_AVAILABLE:
                        break
                except:
                    pass
                
                try:
                    FIRST_AVAILABLE = PRODUCT_DETAILS.find('th',text=re.compile(r'.*Date first listed on Amazon.*')).findNext('td').text
                    if FIRST_AVAILABLE:
                        break
                except:
                    pass
                
                FIRST_AVAILABLE = '[!Error: FIRST_AVAILABLE Not Found]'
                return FIRST_AVAILABLE
            
            try:
                FIRST_AVAILABLE = ' '.join(''.join(FIRST_AVAILABLE).split())
                FIRST_AVAILABLE = datetime.strptime(FIRST_AVAILABLE, '%B %d, %Y').date()
            except:
                FIRST_AVAILABLE = '[!Error: FIRST_AVAILABLE Could Not Parse]'
            return FIRST_AVAILABLE




        def findTechnicalDetailsBlock(self, content):

            while True:
                try:
                    TECHNICAL_DETAILS =    content.find('div',attrs={"id":"prodDetails"})
                    if TECHNICAL_DETAILS:
                        break
                except:
                    pass
                
                try:
                    TECHNICAL_DETAILS =    content.find('div',attrs={"id":"productDetails_feature_div"})
                    if TECHNICAL_DETAILS:
                        break
                except:
                    pass        
                
                TECHNICAL_DETAILS = '[!Error: TECHNICAL_DETAILS Not Found]'
                return TECHNICAL_DETAILS

            return TECHNICAL_DETAILS



        def findAllTechDetails(self, TECHNICAL_DETAILS):
            
            TECH_DETAILS_DICT = {}   
            
            while True:
                try:
                    DETAILS = TECHNICAL_DETAILS.find('table',attrs={'id':'productDetails_techSpec_section_1'}).find_all('tr')
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
                


        def findMoreDetails(self, TECHNICAL_DETAILS):
            
            while True:
                try:
                    MORE_DETAILS = TECHNICAL_DETAILS.find('table',attrs={'id':'productDetails_techSpec_section_1'})
                    if MORE_DETAILS:
                        break
                except:
                    pass
                
                try:
                    MORE_DETAILS = TECHNICAL_DETAILS.find('table',attrs={'id':'productDetails_detailBullets_sections1'})
                    if MORE_DETAILS:
                        break
                except:
                    pass
                
                MORE_DETAILS = '[!Error: MORE_DETAILS Not Found]'
                return MORE_DETAILS
        #    print(MORE_DETAILS)
            
            return MORE_DETAILS



        def findBrandName(self, content, MORE_DETAILS):

            while True:
                try:
                    BRAND = MORE_DETAILS.find('th',text=re.compile(r'.*Brand Name.*')).findNext('td').contents[0]
                    if BRAND:
                        break
                except:
                    pass
                
                try:
                    BRAND =  content.find('a',attrs={'id':'bylineInfo'}).text
                    if BRAND:
                        break
                except:
                    pass
                
                BRAND = '[!Error: BRAND Not Found]'
                return BRAND
            try:
                BRAND = ' '.join(''.join(BRAND).split())
            except:
                BRAND = '[!Error: BRAND Could Not Parse]'
                
            return BRAND



        def findModelNumber(self, MORE_DETAILS, TECHNICAL_DETAILS):

            while True:
                try:
                    PART_NUMBER = MORE_DETAILS.find('th',text=re.compile(r'.*Item model number.*')).findNext('td').contents[0]
                    if PART_NUMBER:
                        break
                except:
                    pass
                

                try:
                    PART_NUMBER = TECHNICAL_DETAILS.find('th',text=re.compile(r'.*Item model number.*')).findNext('td').contents[0]
                    if PART_NUMBER:
                        break
                except:
                    pass      
                
                
                PART_NUMBER = '[!Error: PART_NUMBER Not Found]'
                return PART_NUMBER
            
            try:
                PART_NUMBER = ' '.join(''.join(PART_NUMBER).split())
            except:
                PART_NUMBER = '[!Error: PART_NUMBER Could Not Parse]'
            return PART_NUMBER



        def findItemWeight(self, MORE_DETAILS, TECHNICAL_DETAILS):
           RAW_ITEM_WEIGHT = None
           
           while RAW_ITEM_WEIGHT is None:
                try:
                    RAW_ITEM_WEIGHT = MORE_DETAILS.find('th',text=re.compile(r'.*Item Weight.*')).findNext('td').contents[0]
                except:
                    pass

                try:
                    RAW_ITEM_WEIGHT = TECHNICAL_DETAILS.find('th',text=re.compile(r'.*Item Weight.*')).findNext('td').contents[0]
                except:
                    pass 
                break
           try:
                PRODUCT_WEIGHT = re.sub(r"(\d) .*",r"\1",RAW_ITEM_WEIGHT)
                PRODUCT_WEIGHT = ' '.join(''.join(PRODUCT_WEIGHT.split())).replace(" ","")
           except:
                PRODUCT_WEIGHT = '[!Error: PRODUCT_WEIGHT Not Found]'
        #    print(SHIPPING_WEIGHT)


           try:
               PRODUCT_WEIGHT_UNIT = re.sub(r".*\d (.*)",r"\1",RAW_ITEM_WEIGHT)
               PRODUCT_WEIGHT_UNIT = ' '.join(''.join(PRODUCT_WEIGHT_UNIT.split())).replace(" ","")
           except:
               PRODUCT_WEIGHT_UNIT = '[!Error: PRODUCT_WEIGHT_UNIT Not Found]'
        #    print(SHIPPING_WEIGHT_UNIT)

           ITEMWEIGHT = dict();
           ITEMWEIGHT['PRODUCT_WEIGHT'] = PRODUCT_WEIGHT
           ITEMWEIGHT['PRODUCT_WEIGHT_UNIT'] = PRODUCT_WEIGHT_UNIT
           return ITEMWEIGHT


        def findDimensions(self, MORE_DETAILS, TECHNICAL_DETAILS):

            while True:
                
                try:
                    DIMENSIONS = ' '.join(''.join(MORE_DETAILS.find('th',text=re.compile(r'.*Product Dimensions.*')).findNext('td').contents[0]).split())
                    if DIMENSIONS:
                        break
                except:
                    pass
                
                try:
                    DIMENSIONS = ' '.join(''.join(TECHNICAL_DETAILS.find('th',text=re.compile(r'.*Product Dimensions.*')).findNext('td').contents[0]).split())
                    if DIMENSIONS:
                        break
                except:
                    pass        
                break

            try:
                DIMENSIONS_UNIT = ' '.join(''.join(re.sub('.*\d','',DIMENSIONS.split('x')[2])).split())
            except:
                DIMENSIONS_UNIT = '[!Error: DIMENSIONS_UNIT Not Found]'
                
            try:
                DIMENSIONS = DIMENSIONS.replace(DIMENSIONS_UNIT,'').replace(' ','').split('x')
            except:
                DIMENSIONS = '[!Error: DIMENSIONS Not Found]'
            
            DIMS = dict();
            DIMS['DIMENSIONS'] = DIMENSIONS
            DIMS['DIMENSIONS_UNIT'] = DIMENSIONS_UNIT
            return DIMS


        def findStockMessage(self, content):
            
            while True:
                try:
                    STOCK_MESSAGE = content.find('div',attrs={'id':'availability'}).text
                    if STOCK_MESSAGE:
                        break
                except:
                    pass
                STOCK_MESSAGE = ''
                return STOCK_MESSAGE
            
            
            if "left in stock" in STOCK_MESSAGE:
                try:
                    STOCK_MESSAGE =' '.join(''.join(re.sub(r".*(Only)",r"\1",STOCK_MESSAGE)).split())
                    return STOCK_MESSAGE
                except:
                    STOCK_MESSAGE = '[!Error: STOCK_MESSAGE Could Not Parse]'

            try:
                STOCK_MESSAGE = ' '.join(''.join(STOCK_MESSAGE).split())
                return STOCK_MESSAGE
            except:
                STOCK_MESSAGE = '[!Error: STOCK_MESSAGE Could Not Parse]'
                    
                
            return STOCK_MESSAGE




        def findZipCode(self, content):
            while True:
                try:
                    ZIP_CODE = content.find('div',attrs={'id':'contextualIngressPtLabel_deliveryShortLine'}).text
                    if ZIP_CODE:
                        break
                except:
                    pass
                
                ZIP_CODE = '[!Error: ZIP_CODE Not Found]'
                return ZIP_CODE
            
            try:
                ZIP_CODE = ' '.join(''.join(re.sub(r".* ",r"",ZIP_CODE)).split())
            except:
                ZIP_CODE = '[!Error: ZIP_CODE Could Not Parse]'
            
            return ZIP_CODE 






