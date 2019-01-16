from sqlalchemy import create_engine, update
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound

from datetime import datetime

from ORM.tables.tblUrlQueue import *
from ORM.tables.tblRetailer import *
from ORM.tables.tblStatic import *
from ORM.tables.tblDynamic import *
from ORM.tables.tblUrls import *


Engine = create_engine('mysql+pymysql://root:qwerty1!@127.0.0.1/dataFetch')
Session = sessionmaker(bind=Engine)
session = Session()

class CrawlResults():

	def __init__(self, dic):
		print('start crawl results')
		self.dic = dic
		self.stadic = Static(self.dic)
		self.url = self.stadic.staUrlId
		self.retId = self.stadic.staRetId 
		self.childId = self.stadic.staChildIdentifier
		self.urldic = Urls(self.url, self.retId)
		self.dyndic = Dynamic(self.dic)
		self.dyndic.dynRetId = self.retId

	def Upsert_Data(self):
		try:
			self.URLID = CrawlResults.CheckPK_URL(self, self.url, self.retId)
		except Exception as e:
			print(e)

		try:
			self.stadic.staUrlId = self.URLID
			STAID = CrawlResults.CheckPK_STA(self, self.retId, self.URLID, self.childId)
		except Exception as e:
			print(e)

		# try:
		self.dyndic.dynStaId = STAID
		CrawlResults.Insert_tblDynamic(self.dyndic)
		# except Exception as e:
		# 	print(e)

	def CheckPK_URL(self, url, retId):
		try:
			print('try check pk URL')
			URLID = session.query(Urls).filter(Urls.urlUrl == url, Urls.urlRetId == retId).first().urlId
			print('pk found URL')
			CrawlResults.Update_tblUrl(self.urldic, URLID)
			return URLID
		except NoResultFound:
			return
		except:
			URLID = CrawlResults.Insert_tblUrl(self.urldic)
			return URLID

	def Insert_tblUrl(urldic):
		print('try insert tblurl')
		urldic.urlDateInserted = datetime.now().replace(microsecond=0)
		urldic.urlDateModified = datetime.now().replace(microsecond=0)
		urldic.urlBadUrl = 0
		urldic.urlBadUrlHistory = 0
		urldic.urlPriority = 1
		session.add(urldic)
		session.commit()
		print('inserted tblurl')
		session.refresh(urldic)
		URLID = (urldic.urlId)
		session.flush()
		return URLID

	def Update_tblUrl(urldic, UurlId):
		pass

	def CheckPK_STA(self, retId, URLID, CHILDID):
		try:
			print('try check pk sta')
			STAID = session.query(Static).filter(Static.staRetId == retId, Static.staUrlId == URLID, Static.staChildIdentifier == CHILDID).first().staId
			print("sta pk found")
			CrawlResults.Update_tblStatic(self.stadic, STAID)
			return STAID
		except:
			print("sta pk not found")
			print(self.stadic)
			STAID = CrawlResults.Insert_tblStatic(self.stadic)
			return STAID

	def Insert_tblStatic(self):
		print("try insert tblstatic")
		session.add(self)
		try:
			session.commit()
		except Exception as e:
			print(e)
		session.refresh(self)
		STAID = (self.staId)
		print('inserted into tblstatic')
		session.flush()
		return STAID

	def Update_tblStatic(self, STAID):
		print("try update tblstatic")
		print(self)
		print(STAID)
		self.staCrawlTime = datetime.now().replace(microsecond=0)
		print('need to add update logic for tblstatic')
		# x = update(Urls.__table__).\
		# 		where(Urls.urlId == UurlId).\
		# 		values(urlBadUrl=1)
		# print(x.execution_options())
		# Engine.execute(x)
		# session.flush()
		# pass

	def Insert_tblDynamic(self):
		print("try insert tbldynamic")
		self.staCrawlTime = datetime.now().replace(microsecond=0)
		session.add(self)
		session.commit()
		session.refresh(self)
		print('inserted into tbldynamic' + str(self.dynStaId))