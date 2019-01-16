#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 10:53:32 2018

@author: joe
"""

from selenium import webdriver
from PIL import Image

# DRIVER = '/usr/local/bin/chromedriver'

# driver = webdriver.Chrome(DRIVER)
# driver.get('https://www.amazon.com/dp/B071G83CNN')
#screenshot = driver.save_screenshot('my_screenshot3.png')
#driver.quit()

# print(driver.page_source.encode("utf-8"))
 


img = Image.open('my_screenshot3.png')


cropped = img.crop((928,262,1064,315))

cropped.save('cropped_img3.png')


from PIL import Image

img = Image.open('my_screenshot3.png')


cropped = img.crop((928,262,1064,315))

cropped.save('cropped_img2.png')