import requests
import sys
from bs4 import BeautifulSoup
import csv
import pandas as pd
import requests
import time
import json

API_ENDPOINT = "http://localhost:8000/crypto/"
API_KEY = "b*8p4e%!rk#hzm04$@j@6ie54&*wg+cpmmua0f_-(h4k(qpq0!"
METHOD = "PUT"

cryptos = []
index = 0
url_index = 0

while True:
    # URL to scrape data from
    CryptoUrl = "https://finance.yahoo.com/cryptocurrencies?count=100&offset=" + str(url_index)

    # Send a GET request to retrieve html
    r = requests.get(CryptoUrl)
    data = r.text

    # Load the data into soup
    soup = BeautifulSoup(data, 'lxml')


    # For Loop - Yahoo Finance requires us to crawl through specific
    # attributes to find data
    for listing in soup.find_all('tr', attrs={'class':'simpTblRow'}):
        listing_dict = {}
        listing_dict["id"] = index
        for name in listing.find_all('td', attrs={'aria-label':'Name'}):
            listing_dict["name"] = name.text
        for price in listing.find_all('td', attrs={'aria-label':'Price (Intraday)'}):
            listing_dict["price"] = price.text.replace(',', '')
        for change in listing.find_all('td', attrs={'aria-label':'Change'}):
            listing_dict["change"] = change.text.replace(',', '')
        for percentChange in listing.find_all('td', attrs={'aria-label':'% Change'}):
            listing_dict["percentChange"] = percentChange.text
        index += 1

        cryptos.append(listing_dict)

    if url_index != 100:
        url_index += 100
    else:
        if METHOD == "POST":
            requests.post(url=API_ENDPOINT, json=json.dumps(cryptos))
            sys.exit()

        requests.put(url=API_ENDPOINT, json=json.dumps(cryptos))
        url_index = 0
        index = 0
        time.sleep(60)
