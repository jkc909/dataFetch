
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Date, SmallInteger, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from datetime import datetime
from dbBase import Base


class Static(Base):
	__tablename__ = 'tblStatic'
	staId = Column(Integer, autoincrement = True, primary_key = True)
	# staUrlId = Column(Integer, ForeignKey('tblUrls.urlId'), primary_key = True)
	staRetId = Column(Integer, ForeignKey('tblRetailer.retId'))
	staProductName = Column(String(255))
	staBreadcrumb = Column(String(255))
	staOptionName = Column(String(255))
	staChildIdentifier = Column(String(255), primary_key = True)
	staParentIdentifier = Column(String(255))
	staUrlId = Column(Integer, ForeignKey('tblUrls.urlId'), primary_key = True)
	staPartNumber = Column(String(255))
	staImageCount = Column(Integer)
	staDescription = Column(String(10025))
	staMainImage = Column(String(255))
	staShippingWeight = Column(Numeric)
	staShippingWeightUnit = Column(String(50))
	staBestSeller1 = Column(String(255))
	staBestSeller2 = Column(String(255))
	staBestSeller3 = Column(String(255))
	staFirstAvailable = Column(Date())
	staBrand = Column(String(255))
	staItemWeight = Column(Numeric)
	staItemWeightUnit = Column(String(50))
	staDimensions = Column(String(255))
	staDimensionsUnit = Column(String(255))
	staAplus = Column(Boolean)
	staLastCrawl = Column(Integer, ForeignKey('tblCrawlResult.crlId'))


	def __init__(self, urlId, retId, crlId, data):
		self.staUrlId = urlId
		self.staRetId = retId
		self.staLastCrawl = crlId
		self.staProductName = data['staProductName']
		self.staProductName = data['staProductName']
		self.staBreadcrumb = data['staBreadcrumb']
		self.staOptionName = data['staOptionName']
		self.staChildIdentifier = data['staChildIdentifier']
		self.staParentIdentifier = data['staParentIdentifier']
		self.staPartNumber = data['staPartNumber']
		self.staImageCount = data['staImageCount']
		self.staDescription = data['staDescription']
		self.staMainImage = data['staMainImage']
		self.staShippingWeight = data['staShippingWeight']
		self.staShippingWeightUnit = data['staShippingWeightUnit']
		self.staBestSeller1 = data['staBestSeller1']
		self.staBestSeller2 = data['staBestSeller2']
		self.staBestSeller3 = data['staBestSeller3']
		self.staFirstAvailable = data['staFirstAvailable']
		self.staBrand = data['staBrand']
		self.staItemWeight = data['staItemWeight']
		self.staItemWeightUnit = data['staItemWeightUnit']
		self.staDimensions = data['staDimensions']
		self.staDimensionsUnit = data['staDimensionsUnit']
		self.staAplus = data['staAplus']
		