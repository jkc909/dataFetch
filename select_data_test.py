from ORM.tables.tblCaptcha import *
from ORM.tables.tblCrawlResult import *
from ORM.tables.tblDynamic import *
from ORM.tables.tblHeaders import *
from ORM.tables.tblPLCrawlResult import *
from ORM.tables.tblRetailer import *
from ORM.tables.tblStatic import *
from ORM.tables.tblUrlQueue import *
from ORM.tables.tblUrls import *


from engine_session import create_session

class get_data():
	def __init__(self):
		self.Session = create_session().return_session()

	def hello(self):
		retailer = self.Session.query(Retailer)
		print(retailer[0].__dict__)
		# print(dict(retailer[0]))

	def get_static(self):
		static = self.Session.query(Static)
		results = []
		for r in static: 
			r.__dict__.pop('_sa_instance_state', None)
			results.append(r.__dict__)
		return results

test = get_data().get_static()
print(test[0])