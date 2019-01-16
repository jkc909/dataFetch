from sqlalchemy import update
from datetime import datetime

from ORM.tables.tblRequestResult import *
from ORM.tables.tblUrls import *

class insert_request():
	def __init__(self, create_session, engine, url, retId, \
				block, hedId, status, captcha):
		self.session = create_session()
		self.url = url
		self.retId = retId
		self.block = block
		self.hedId = hedId
		self.status = status
		self.captcha = captcha
		self.url_results = self.session.query(Urls).filter(Urls.urlUrl == self.url).all()
		self.urlId = insert_request.checkUrl(self)
		insert_request.insert(self)
		self.session.close()

	def checkUrl(self):
		try:
			self.urlId = self.url_results[0].urlId
		except:
			insert_url = Urls(self.url, self.retId)
			self.session.add(insert_url)
			self.session.commit()
			self.session.refresh(insert_url)
			self.urlId = insert_url.urlId	
		return self.urlId		


	def insert(self):
		reqObject = RequestResult(self.urlId, self.retId, self.hedId, self.captcha, self.status, self.block)
		self.session.add(reqObject)
		self.session.commit()
		self.session.flush()



