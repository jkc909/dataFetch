from bs4 import BeautifulSoup
import requests

class make_request():
	def __init__(self, url, headers):
		self.headers = headers
		self.url = url
		print(self.url)
		self.asin = self.url.replace('https://www.amazon.com/dp/','')
		print(self.asin)

	def request(self):
		print("request initiated")

		try:
			filename = 'amazonfiles/amazon_'+self.asin+".html"
			f = open (filename, "r+")
			raw_html = f.read()
			# print(raw_html)
			f.close()
			bs_format = BeautifulSoup(raw_html, 'html5lib')
			f.close()
			status_code = 200

		except:
			raw_html = requests.get(self.url, headers=self.headers, timeout=5)
			status_code = raw_html.status_code
			bs_format = BeautifulSoup(raw_html.text, 'html5lib')

			filename = 'amazonfiles/amazon_'+self.asin+".html"
			f = open (filename, "w+")
			f.write(raw_html.text)
			f.close()
			print('from file')

		return(bs_format, status_code)