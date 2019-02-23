import json
import requests

class make_request():
	def __init__(self, url, headers):
		self.headers = headers
		self.url = url
		self.childId = self.url.replace('https://www.sweetwater.com/store/detail/','').split('--', 1)[0]
		self.url = "https://www.sweetwater.com/webservices_sw/items/detail/"+self.childId
		print(self.url)

	def request(self):
		print("request initiated")

		try:
			filename = 'retailer2/json_files/'+self.childId+".json"
			f = open (filename, "r+")
			raw_json = f.read()
			f.close()
			json_payload = json.loads(raw_json)
			status_code = 200
			# print(json_payload)

		except:
			raw_json = requests.get(self.url, headers={'DNT': '1', 
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/42.0'}, timeout=5)
			status_code = raw_json.status_code
			if status_code == 403:
				import code; code.interact(local=dict(globals(), **locals()))
			json_payload = raw_json.json()

			filename = 'retailer2/json_files/'+self.childId+".json"
			f = open (filename, "w+")
			f.write(raw_json.text)
			f.close()

		return(json_payload, status_code)

