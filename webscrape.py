#!/usr/bin/env python

from lxml import html
import requests

#   sudo pip install lxml
def suro_ws_webpage_html(url):
    page = requests.get(url)
    tree = html.fromstring(page.text)
    # tree.xpath()

def suro_ws_secure_webpage_html(url, user='None', pw='None', verify=True, 
                                cookie_name='None', coookie_val=r''):
    use_auth = False
    use_cookie = False

    if user != 'None':
       auth = (user, pw)
       use_auth = True

    if cookie_name != 'None':
       cookie = { cookie_name : cookie_val }
       use_cookie = True

    if use_auth and use_cookie:
       page = requests.get(url, verify=verify, auth=auth, cookies=cookie)
    else:
       if use_auth:
           page = requests.get(url, verify=verify, auth=auth)
       if use_cookie:
           page = requests.get(url, verify=verify, cookies=cookie)
       
    page = requests.get(url)
    tree = html.fromstring(page.text)
    # tree.xpath()

# If the webpage contains JS, we need selenium binding
# selenium's webdriver needs a driver, i.e. browser - firefox/chrome
# firefox/chrome needs a display - thus we need pyvirtualdisplay
# Still we need Xvfb
#
# sudo pip install selenium
# sudo yum install firefox
# sudo pip install xvfbwrapper
# sudo pip install pyvirtualdisplay
# sudo yum install Xvfb
from selenium import webdriver
from xvfbwrapper import Xvfb
def suro_ws_js_enabled_page():
    vdisplay = Xvfb()
    vdisplay.start()

    browser = webdriver.Firefox()
    browser.get('http://www.google.com')
    print browser.title
    browser.quit()
 
    vdisplay.stop()

    
