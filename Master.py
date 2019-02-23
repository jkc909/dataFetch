from engine_session import create_session
from dblistener import event_listener
from get_url_headers import get_url_headers
from crawl_initiate import crawl_sorter
from insert_crawl_results import update_database


class start_and_run():
	def __init__(self):
		self.Session = create_session().return_session()
	
	def start(self):

		print("db listener")
		urlId_retId = event_listener(self.Session).return_value()

		print("get url")
		url_to_crawl = get_url_headers(self.Session,urlId_retId).return_value
		print("initiate crawl")

		data = crawl_sorter(url_to_crawl).return_value()
		print("store crawl result")

		final_payload = (self.Session,\
						urlId_retId[0],\
						urlId_retId[1],\
						data[2],\
						data[0][0],\
						data[0][1],\
						data[1][0],\
						data[1][1],\
						url_to_crawl[1][1],\
						data[0][2])
		update = update_database(final_payload).return_value()
		print(update)

import time		
while True:
	start_and_run().start()
	time.sleep(1)
