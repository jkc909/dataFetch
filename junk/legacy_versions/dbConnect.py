from sqlalchemy import create_engine, update
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound

from datetime import datetime

from tblRetailer import Retailer
from tblUrlQueue import UrlQueue
from tblStatic import Static
from tblUrls import Urls
from tblDynamic import Dynamic

from dbCrawlResults import CrawlResults



Engine = create_engine('mysql+pymysql://root:qwerty1!@127.0.0.1/dataFetch')
Session = sessionmaker(bind=Engine)
session = Session()


from retID_1_spider_test2 import *




# from tblStatic import Static

# with open(r'overstock_test13.html', "r") as file:
# 	page = file.read()

# input = Data(page)

# data = input.data()
    # print(page)





# input = Data(page)

# data = input.data()

# for i in data:
#     print(i, ":", data[i])

# print(data["staProductName"])


# literally = Static(data)
# literally.staUrlId = '123'
# literally2 = Dynamic(data)

# session.add(literally)
# session.add(literally2)
# session.commit()




# print(testurl5.urlUrl)

# class Merge_tblUrl():

# 	def __init__(self, dic):
# 		self.url = dic.urlUrl
# 		self.retId = dic.urlRetId 
# 		self.dic = dic


# 	def Upsert(self):
# 		try:
# 			ID = Merge_tblUrl.CheckPK(self, self.url, self.retId)
# 			Merge_tblUrl.Update_tblUrl(self.dic, ID)
# 		except:
# 			Merge_tblUrl.Insert_tblUrl(self.dic)

# 	def CheckPK(self, url, retId):
# 		try:
# 			ID = session.query(Urls).filter(Urls.urlUrl == url, Urls.urlRetId == retId).first().urlId
# 			print(ID)
# 			return ID
# 		except NoResultFound:
# 			return

# 	def Insert_tblUrl(dic):
# 		dic.urlDateInserted = datetime.now().replace(microsecond=0)
# 		dic.urlDateModified = datetime.now().replace(microsecond=0)
# 		dic.urlBadUrl = 0
# 		dic.urlBadUrlHistory = 0
# 		dic.urlPriority = 1
# 		print('heldfdfasfasdlo')
# 		session.add(dic)
# 		session.commit()

# 	def Update_tblUrl(dic, UurlId):
# 		pass
# 		# x = update(Urls.__table__).\
# 		# 		where(Urls.urlId == UurlId).\
# 		# 		values(urlBadUrl=1)
# 		# print(x.execution_options())
# 		# Engine.execute(x)
# 		# session.flush()








path = 'amazonfiles/'
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
		# print(page)
	# with open(file, "r") as x:
	# 	print(str(x))
	# 	file = x.read()
	# print(page)
	input = Data(page)
	data = input.data()
	# print(data)
	CrawlResults(data).Upsert_Data()
	session.flush()
	session.close()
	file.close()



# print() #.filter_by(**kwargs).first()



# CrawlResults(data).Upsert_Data()

# import amazonfiles


# x = /amazonfiles

# for file in os.listdir(x):
# 	print(file)



# print(os.listdir('amazonfiles'))







# Merge_tblUrl(testurl5).Upsert()
# session.add(testurl5)


	# if session.query(UrlQueue).filter_by(qrlUrl = val).first() is None:
	# 	print("none")
	# else:
	# 	print("some?")

# print()

# Merge_tblUrl('hello1', 1)

# print(CheckPK('hello1', 3))

# for x in session.query(UrlQueue):
# 	print(x.qrlUrl)

# print(session.all())


# session.commit()

# session.refresh(testurl4)


# print(testurl4.qrlId)




# result = (engine.execute('select qrlUrl from tblUrlQueue;')).fetchall()
# # result1 = result.fetchall()

# print(result)


