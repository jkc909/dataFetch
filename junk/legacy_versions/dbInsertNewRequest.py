from ORM.tables.tblRequestResult import *

# dbInsertNewRequest.py

		# crawl_sorter.insert_new_request(self)

def insert_new_request(self):
	insert_request(self.sessionmaker, \
					self.createngine,  \
					self.url, \
					self.retId, \
					self.blocked, \
					self.header_id, \
					self.status_code, \
					self.captcha)