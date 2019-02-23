
from sqlalchemy import Column, Integer, String, Boolean, DateTime, SmallInteger, ForeignKey, func
from sqlalchemy.orm import relationship
from sqlalchemy.schema import PrimaryKeyConstraint
from datetime import datetime
from dbBase import Base

class Urls(Base):
	__tablename__ = 'tblUrls'

	urlId = Column(Integer, autoincrement = True, primary_key = True, unique=True)
	urlUrl = Column(String(255), primary_key = True, unique=True)
	urlRetId = Column(Integer, ForeignKey('tblRetailer.retId'))
	urlBadUrl = Column(Boolean)
	urlBadUrlReason = Column(Integer)
	urlBadUrlLastDate = Column(DateTime)
	urlBadUrlHistory = Column(Integer)
	urlDateInserted = Column(DateTime, default=func.now())
	urlDateModified = Column(DateTime)
	urlPriority = Column(SmallInteger)
	urlNotes = Column(String(255))
	qrl = relationship('UrlQueue')
	sta = relationship('Static')
	crl = relationship('CrawlResult')

	def __init__(self, urlUrl, urlRetId):
		self.urlUrl = urlUrl
		self.urlRetId = urlRetId
