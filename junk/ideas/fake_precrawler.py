#!/Users/joe/dataFetch/DEV/
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 22:13:04 2018

@author: joe
"""

#from sqlalchemy.engine.url import URL
from sqlalchemy import create_engine
from retID_1_spider_test2 import *
from headers import getHeader
import time
#import requests


from headers import getHeader
import requests

headerz = getHeader()
print(headerz)

ASINS = ['BB00VVNOMGI', 'B07JZTYYWR']

for a in ASINS:
	URL = 'https://www.amazon.com/dp/'+a
	FILEname = 'amazonfiles/amazon_'+a+".html"
	print(URL)
	print(FILEname)
	r = requests.get(URL, headers=headerz, timeout=5)
	f = open (FILEname, "w+")
	f.write(r.text)
	f.close()
	time.sleep(5)

#






# r = requests.get('https://www.amazon.com/dp/B073SQ21CT', headers=headerz, timeout=5)

# f = open ("amazonfiles/overstock_test1212.html", "w+")
# #
# f.write(r.text)
# #
# f.close()
#




#https://medium.com/python-pandemonium/6-things-to-develop-an-efficient-web-scraper-in-python-1dffa688793c

#try:
#    # your logic is here
#
#except requests.ConnectionError as e:
#    print("OOPS!! Connection Error. Make sure you are connected to Internet. Technical Details given below.\n")
#    print(str(e))
#except requests.Timeout as e:
#    print("OOPS!! Timeout Error")
#    print(str(e))
#except requests.RequestException as e:
#    print("OOPS!! General Error")
#    print(str(e))
#except KeyboardInterrupt:
#    print("Someone closed the program")
#





# from retID_1_spider_test2 import *
# from tblStatic import Static

# with open(r'overstock_test13.html', "r") as file:
#     page = file.read()

# input = Data(page)

# data = input.data()

# for i in data:
#     print(i, ":", data[i])

# print(data["staProductName"])


# print(Static(data).staBreadcrumb)





#
#ASINS = [
#        'B0000WS0SC',
#        'B00G31YMVS',
#        'B00CAKSVTU',
#        'B00684KFFW',
#        'B01N8ZRV3V',
#        'B01HZ8UG62',
#        'B07D1GNLDM',
#        'B00V5BP2H4',
#        'B004M8YPKM',
#        'B074KCBLQ8',
#        'B07BKQ6M22',
#        'B07BHYZRYG'
#        ]
#
#for i in ASINS:
#    url = ("https://www.amazon.com/dp/" + i)
#    filename = (i + ".html")
#    print(url)
#    print(filename)






     

#script =("INSERT INTO new_schema1.test_table1 "
#         "(col1, col2) values ('",
#         data.get('NAME'),
#         "', "
#         "99999"
#         ")"
#         )






#s = ''.join(script)
    
#print(s)

#engine.execute(s)

#
#engine.execute('insert into new_schema1.test_table1 '
#               '(col1, col2) '
#               'values (',
#               data.get('NAME'),
#               ', 6)')
