
from summoner import Data
import block_check

import time

class crawl_sorter():
	def __init__(self, url_header):
		print(url_header)
		self.url = url_header[0][0]
		self.retId = url_header[0][1]
		self.headers = url_header[1][0]
		self.hedId = url_header[1][1]
		self.response = self.get_response()
		
	def get_response(self):
		if (self.retId == 1):
			print("AMAZON")
			from generic_request import make_request
			response = make_request(self.url, self.headers).request()
			return response

	def return_value(self):
		time.sleep(1)
		bot_check = block_check.block_check(self.response[0])
		if bot_check[0] == 2:
			return(((''),(''),('')), bot_check, self.response[1])
		else:
			parsed_data = Data(self.response[0],self.retId).payload()
			if parsed_data[2]:
				return(parsed_data, (1,''), self.response[1])
			else:
				return(((''),(''),('')),(3,''),self.response[1])

		

