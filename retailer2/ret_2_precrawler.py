from bs4 import BeautifulSoup
# import requests
import json


from dbBase import Base
from engine_session import create_session

from tblUrlQueue import *
from tblUrls import *


session = create_session().return_session()



# metadata = MetaData(bind=Engine)



path = 'html_files/'
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
		# page = page.encode('ascii', 'ignore').decode('ascii')
		# print(page)
	# with open(file, "r") as x:
	# 	print(str(x))
	# 	file = x.read()
	# print(page)
	bs_html = BeautifulSoup(page, 'html.parser', from_encoding='utf-8')
	file.close()
	# print(bs4_parse)
	printme = bs_html.findAll('div',attrs={'class':'product-card__info'})
	for p in printme:
		# print(p.encode("utf8"))
		url = "https://www.sweetwater.com" + str(p.find('a')["href"])
		# print(url)
		new_url = Urls(url, 2)
		session.add(new_url)
		session.commit()
		session.refresh(new_url)
		urlid = new_url.urlId
		new_urlQueue = UrlQueue(urlid, 2)
		session.add(new_urlQueue)
		session.commit()
		session.flush()
		print("added url: " + str(url))
		# break
	
	# input = Data(page)
	# data = input.data()
	# # print(data)
	# CrawlResults(data).Upsert_Data()
	# session.flush()
	# session.close()

