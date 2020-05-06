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
METHOD = "POST"

index = 0
url_index = 0

# URL to scrape data from
CryptoUrl = "https://finance.yahoo.com/cryptocurrencies?count=100&offset=" + str(url_index)

# Send a GET request to retrieve html
r = requests.get(CryptoUrl)
data = r.text

# Load the data into soup
soup = BeautifulSoup(data, 'lxml')

crypto = {
    "id": [],
    "name": [],
    "price": [],
    "change": [],
    "percentChange": []
}


# For Loop - Yahoo Finance requires us to crawl through specific
# attributes to find data
for listing in soup.find_all('tr', attrs={'class':'simpTblRow'}):
    for name in listing.find_all('td', attrs={'aria-label':'Name'}):
        crypto["name"].append(name.text)
    for price in listing.find_all('td', attrs={'aria-label':'Price (Intraday)'}):
        crypto["price"].append(price.text.replace(',', ''))
    for change in listing.find_all('td', attrs={'aria-label':'Change'}):
        crypto["change"].append(change.text)
    for percentChange in listing.find_all('td', attrs={'aria-label':'% Change'}):
        crypto["percentChange"].append(percentChange.text.replace('%', ''))

    crypto["id"].append(index)
    index += 1

requests.post(url=API_ENDPOINT, data=crypto)
