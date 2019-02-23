from bs4 import BeautifulSoup
import requests
import json


from dbBase import Base
from engine_session import create_session

from tblUrlQueue import *
from tblUrls import *


session = create_session().return_session()


path = 'html_files/'
import os
for file in os.listdir(path):
	if file == '.DS_Store':
		continue
	ok = str(path+file)
	assert os.path.isfile(path+file)
	with open(ok, "rb") as file:
		page = file.read()
		# print(page)
		file.close()
	bs4mat = BeautifulSoup(page, 'html5lib')
	links = bs4mat.findAll('a',attrs={'class':'s-access-detail-page'})
	# print(links[0])
	# print(ok)
	x = 0
	for p in links:
		if ("Bundle" not in p['href'] and "Eurorack" not in p['href'] and "Floppy" not in p['href'] and "Emulator" not in p['href']):
			try:
				asin = p['href'].split('/')[5]
			except:
				pass
			url = 'https://www.amazon.com/dp/' + asin

			new_url = Urls(url, 1)
			
			try:
				session.add(new_url)
				session.commit()
				session.refresh(new_url)
				urlid = new_url.urlId
				new_urlQueue = UrlQueue(urlid, 1)
				session.add(new_urlQueue)
				session.commit()
				session.flush()
				print("added url: " + str(url) + " " + str(x))
			except Exception as e:
				session.rollback()
			# 	pass
				# print(e)
			x+=1
		else:

			try:
				asin = p['href'].split('/')[5]
			except:
				pass
			url = 'https://www.amazon.com/dp/' + asin

			print("'"+url+"',")











# urls = ('https://www.amazon.com/Synthesizers-Workstations/b?ie=UTF8&node=11970041','https://www.amazon.com/s/ref=lp_11970041_pg_2/147-8034152-5909534?rh=n%3A11091801%2Cn%3A%2111965861%2Cn%3A11969981%2Cn%3A11970001%2Cn%3A11970041&page=2&ie=UTF8&qid=1549385936','https://www.amazon.com/s/ref=sr_pg_3?rh=n%3A11091801%2Cn%3A%2111965861%2Cn%3A11969981%2Cn%3A11970001%2Cn%3A11970041&page=3&ie=UTF8&qid=1549385941&ajr=3')

# # x = 6
# # while x < 48:
# x=1
# for url in urls:

# 	# url = 'https://www.amazon.com/s/ref=sr_pg_'+str(x)+'?rh=n%3A11091801%2Cn%3A%2111965861%2Cn%3A11969981%2Cn%3A11970001%2Cn%3A11970041&page='+str(x)+'&ie=UTF8&qid=1549210717'
# 	print(url)
# 	raw_html = requests.get(url, headers={'DNT': '1', 
# 'Upgrade-Insecure-Requests': '1',
# 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/42.0','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9'}, timeout=5)

# 	raw_html1 = BeautifulSoup(raw_html.text, 'html.parser', from_encoding='utf-8')

# 	filename = 'html_files/synth_landing_'+str(x)+".html"
# 	f = open (filename, "w+")
	

# 	f.write(raw_html.text)
# 	f.close()
# 	import time
# 	x+=1
# 	time.sleep(3)

