
from bs4 import BeautifulSoup
from webbot import Browser
from selenium import webdriver

import requests
import os
import time



web = Browser()
web.go_to('https://my.pltw.org/login') 
web.type('username' ,id ='okta-signin-username')
web.click('Next' , id = 'idp-discovery-submit')
time.sleep(1)
web.type('password',id = "okta-signin-password") 
print('hi')
time.sleep(0.1)
web.click('Sign In', id="okta-signin-submit")
time.sleep(1)
page = web.go_to(url="pltwpagelink")

