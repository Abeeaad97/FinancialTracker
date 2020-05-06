import requests
import sys
from bs4 import BeautifulSoup
import csv
import pandas as pd
import time
import json

API_ENDPOINT = "http://localhost:8000/stocks/"
API_KEY = "b*8p4e%!rk#hzm04$@j@6ie54&*wg+cpmmua0f_-(h4k(qpq0!"
METHOD = "PUT"

stocks = []
index = 0
url_index = 0

while True:
    # URL to scrape data from
    StocksUrl = "https://finance.yahoo.com/most-active?count=100&offset=" + str(url_index)

    # Send a GET request to retrieve html
    r = requests.get(StocksUrl)
    data = r.text

    # Load the data into soup
    soup = BeautifulSoup(data, 'lxml')

    for listing in soup.find_all('tr', attrs={'class':'simpTblRow'}):
        listing_dict = {}
        listing_dict["id"] = index
        for name in listing.find_all('td', attrs={'aria-label':'Name'}):
            listing_dict["name"] = name.text
        for price in listing.find_all('td', attrs={'aria-label':'Price (Intraday)'}):
            listing_dict["price"] = price.text.replace(',', '')
        for change in listing.find_all('td', attrs={'aria-label':'Change'}):
            listing_dict["change"] = change.text.replace(',', '')
        for volume in listing.find_all('td', attrs={'aria-label':'Volume'}):
            listing_dict["volume"] = volume.text
        index += 1

        stocks.append(listing_dict)

    if url_index != 300:
        url_index += 100
    else:
        if METHOD == "POST":
            requests.post(url=API_ENDPOINT, json=json.dumps(stocks))
            sys.exit()

        requests.put(url=API_ENDPOINT, json=json.dumps(stocks))
        url_index = 0
        index = 1
        time.sleep(60)
