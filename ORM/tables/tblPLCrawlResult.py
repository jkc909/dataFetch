from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from datetime import datetime
from dbBase import Base

class PLCrawlResult(Base):
	__tablename__ = 'tblPLCrawlResult'

	crsId = Column(Integer, autoincrement = True, \
							primary_key = True)
	crsCrawlStatus = Column(String(255))
	crl = relationship('CrawlResult')

	def __init__(self, crawl_status):
		self.crsCrawlStatus = crawl_status
