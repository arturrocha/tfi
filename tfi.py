#!/usr/bin/python3
from bs4 import BeautifulSoup
import urllib.request, requests
import wget
import time


class AppURLopener(urllib.request.FancyURLopener):
    version = 'Mozilla/5.0'

url = "https://transportforireland.ie/transitData/PT_Data.html"

opener = AppURLopener()
response = opener.open(url)
soup = BeautifulSoup(response, "html.parser")

#print(soup)
prefix = 'https://transportforireland.ie/transitData/'

for thing in soup.find_all(attrs={'class': 'Page_title'}):
    for url in thing.find_all('a'):
        if not url.get('href').find('google_transit'):
            full_url = prefix + url.get('href')
            print(full_url)
            wget.download(full_url)
            time.sleep(1)
        else:
            pass

