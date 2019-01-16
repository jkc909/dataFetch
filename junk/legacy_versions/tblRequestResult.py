
from sqlalchemy import Column, Integer, String, Boolean, DateTime, SmallInteger, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from dbBase import Base

class RequestResult(Base):
	__tablename__ = 'tblRequestResult'

	reqId = Column(Integer, autoincrement = True, \
							primary_key = True)
	reqCaptcha = Column(String(255))
	reqRetId = Column(Integer, ForeignKey('tblRetailer.retId'))
	reqHedId = Column(Integer, ForeignKey('tblHeaders.hedId'))
	reqStatus = Column(Integer)
	reqBlocked = Column(Boolean)
	reqRequestTime = Column(DateTime)
	reqUrlId = Column(Integer, ForeignKey('tblUrls.urlId'))

	def __init__(self, urlId, retId, hedId, captcha, status, blocked):
		self.reqUrlId = urlId
		self.reqRetId = retId
		self.reqHedId = hedId
		self.reqCaptcha = captcha
		self.reqStatus = status
		self.reqBlocked = blocked
		self.reqRequestTime = datetime.now().replace(microsecond=0)






