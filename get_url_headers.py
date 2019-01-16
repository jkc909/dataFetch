from headers import getHeader
from get_url import get_url

class get_url_headers():
	def __init__(self, session, urlId_retId):
		self.urlId_retId = urlId_retId
		self.session = session
		self.headers = self.get_headers()
		print(self.headers)
		self.url = self.get_url()
		self.return_value = ((self.url,self.urlId_retId[1]), self.headers)

	def return_value(self):
		return self.return_value

	def get_headers(self):
		return getHeader(self.session, self.urlId_retId[1])

	def get_url(self):
		return get_url(self.session, self.urlId_retId)