
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from dbBase import Base


class Retailer(Base):
	__tablename__ = 'tblRetailer'

	retId = Column(Integer, \
					autoincrement = True, \
					primary_key = True)
	retName = Column(String(255), \
					primary_key = True, \
					unique=True)
	qrl = relationship('UrlQueue')
	url = relationship('Urls')
	sta = relationship('Static')
	dyn = relationship('Dynamic')
	crl = relationship('CrawlResult')
	cap = relationship('Captcha')

	def __init__(self, retailer_name):
		self.retName = retailer_name