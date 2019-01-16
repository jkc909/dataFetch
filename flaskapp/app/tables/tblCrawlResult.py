from sqlalchemy import Column, Integer, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship
from app import db

class CrawlResult(db.Model):
	__tablename__ = 'tblCrawlResult'

	crlId = Column(Integer, autoincrement = True, \
							primary_key = True)
	crlRetId = Column(Integer, \
						ForeignKey('tblRetailer.retId'))
	crlHedId = Column(Integer, ForeignKey('tblHeaders.hedId'))
	crlUrlId = Column(Integer, ForeignKey('tblUrls.urlId'))
	crlHttpStatus = Column(Integer)
	crlCrawlStatus = Column(Integer, ForeignKey('tblPLCrawlResult.crsId'))
	crlCrawlTime = Column(DateTime, default=func.now)
	sta = relationship('Static')
	dyn = relationship('Dynamic')
	cap = relationship('Captcha')
	

	def __init__(self, \
				urlId, \
				retId, \
				hedId, \
				http_status, \
				crawl_status):
		self.crlUrlId = urlId
		self.crlRetId = retId
		self.crlHedId = hedId
		self.crlHttpStatus = http_status
		self.crlCrawlStatus = crawl_status

