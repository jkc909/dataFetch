
def block_check(bs):
	try:
		if bs.find('title').text == 'Robot Check':
			print ('BAD NEWS BRO')
			captcha_img = bs.find('form').find('img')["src"]
			print(captcha_img)
		return (2,captcha_img)
	except:
		return (1,'')
		pass
