
from sqlalchemy import Column, Integer, String, Boolean, DateTime, SmallInteger, ForeignKey, func, Float
from sqlalchemy.orm import relationship
from sqlalchemy.schema import PrimaryKeyConstraint
from datetime import datetime
from dbBase import Base

class Matches(Base):
	__tablename__ = 'tblMatches'

	matId = Column(Integer, autoincrement = True, primary_key = True)
	matBaseRetId = Column(Integer, ForeignKey('tblRetailer.retId'), primary_key = True)
	matBaseStaId = Column(Integer, ForeignKey('tblStatic.staId'), primary_key = True)
	matSuggestedStaId = Column(Integer, primary_key = True)
	matApproved = Column(Boolean, default=0)
	matApprovedBy = Column(Integer)
	matApprovedOn = Column(DateTime)
	matSuggestedOn = Column(DateTime, default=func.now())
	matManufacturerScore = Column(Float)
	matPartNumberScore = Column(Float)
	matProductNameScore = Column(Float)
	matPriceScore = Column(Float)
	matAverageScore = Column(Float)

	def __init__(self, payload):
		self.matBaseRetId = payload['matBaseRetId']
		self.matBaseStaId = payload['matBaseStaId']
		self.matSuggestedStaId = payload['matSuggestedStaId']
		self.matManufacturerScore = payload['matManufacturerScore']
		self.matPartNumberScore = payload['matPartNumberScore']
		self.matProductNameScore = payload['matProductNameScore']
		self.matPriceScore = payload['matPriceScore']
		self.matAverageScore = payload['matAverageScore']