from ORM.tables.tblCrawlResult import *
from ORM.tables.tblDynamic import *
from ORM.tables.tblHeaders import *
from ORM.tables.tblPLCrawlResult import *
from ORM.tables.tblRetailer import *
from ORM.tables.tblStatic import *
from ORM.tables.tblUrlQueue import *
from ORM.tables.tblUrls import *

class update_database():
	def __init__(self, payload):
		# import code; code.interact(local=dict(globals(), **locals()))
		self.session = payload[0]
		self.urlId = payload[1]
		self.retId = payload[2]
		self.status = payload[3]
		self.sta_dyn_data = payload[4]
		self.tech_details = payload[5]
		self.crawl_status = payload[6]
		self.captcha = payload[7]
		self.header = payload[8]
		self.childId = payload[9]

	def return_value(self):
		self.insert_new_result()
		self.check_crawl_status()
		self.session.close()

	def insert_new_result(self):
		new_crawl_result = CrawlResult(self.urlId, \
											self.retId, \
											self.header, \
											self.status, \
											self.crawl_status)
		self.session.add(new_crawl_result)
		self.session.commit()
		self.session.refresh(new_crawl_result)
		self.crlId = (new_crawl_result.crlId)
		self.session.flush()

	def check_crawl_status(self):
		if self.crawl_status == 1:
			self.upsert_sta()
			self.insert_dyn()
		elif self.crawl_status == 2:
			# self.insert_captcha()
			pass
		else:
			# here is where you're gonna add BADURL LOGIC
			pass

	def upsert_sta(self):
		try:
			update_staId = self.session.query(Static).\
					filter(Static.staRetId == self.retId, \
							Static.staUrlId == self.urlId, \
							Static.staChildIdentifier == self.childId).\
							with_for_update().\
							first()
			update_staId.staLastCrawl = self.crlId
			self.session.add(update_staId)
			self.session.commit()
			self.staId = update_staId.staId
			self.session.flush()
		except:
			new_sta = Static(self.urlId, \
							self.retId, \
							self.crlId, \
							self.sta_dyn_data)
			self.session.add(new_sta)
			self.session.commit()
			self.staId = new_sta.staId
			self.session.flush()

	def insert_dyn(self):
			new_dyn = Dynamic(self.staId, \
							self.retId, \
							self.crlId, \
							self.sta_dyn_data)
			self.session.add(new_dyn)
			self.session.commit()
			self.staId = new_dyn.dynId
			self.session.flush()			

	def insert_captcha(self):
		new_captcha = Captcha(self.retId, \
								self.crlId, \
								self.captcha)
		self.session.add(new_captcha)
		self.session.commit()
		self.session.flush()

