
from sqlalchemy import Column, Integer, String, Boolean, DateTime, SmallInteger, ForeignKey, Numeric, Date
from sqlalchemy.orm import relationship
from datetime import datetime
from app import db

class Dynamic(db.Model):
	__tablename__ = 'tblDynamic'

	dynId = Column(Integer, autoincrement = True, primary_key = True)
	dynStaId = Column(Integer, ForeignKey('tblStatic.staId'), primary_key = True)
	dynRetId = Column(Integer, ForeignKey('tblRetailer.retId'))
	dynCrlId = Column(Integer, ForeignKey('tblCrawlResult.crlId'))
	dynPrice = Column(Numeric)
	dynStockStatus = Column(Boolean)
	dynSeller = Column(String(255))
	dynShippedBy = Column(String(255))
	dynShipPrice = Column(Numeric)
	dynAnsweredQuestions = Column(Integer)
	dynRating = Column(Numeric)
	dynReviewCount = Column(Integer)
	dynStockMessage = Column(String(255))
	dynZipCode = Column(String(16))
	dynCrawlTime = Column(DateTime())

	def __init__(self, staId, retId, crlId, data):
		self.dynStaId = staId
		self.dynRetId = retId
		self.dynCrlId = crlId
		self.dynPrice = data['dynPrice']
		self.dynStockStatus = data['dynStockStatus']
		self.dynSeller = data['dynSeller']
		self.dynShippedBy = data['dynShippedBy']
		self.dynShipPrice = data['dynShipPrice']
		self.dynAnsweredQuestions = data['dynAnsweredQuestions']
		self.dynRating = data['dynRating']
		self.dynReviewCount = data['dynReviewCount']
		self.dynStockMessage = data['dynStockMessage']
		self.dynZipCode = data['dynZipCode']
		self.dynCrawlTime = data['dynCrawlTime']

