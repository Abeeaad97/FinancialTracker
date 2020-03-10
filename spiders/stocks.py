import requests
import sys
from bs4 import BeautifulSoup
import csv
import pandas as pd
import requests
import schedule
import time

API_ENDPOINT = "http://localhost:8000/stocks/"
API_KEY = "b*8p4e%!rk#hzm04$@j@6ie54&*wg+cpmmua0f_-(h4k(qpq0!"
METHOD = "PUT"

# Data Table
id=[]
names=[]
prices=[]
changes=[]
volumes=[]

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
        for name in listing.find_all('td', attrs={'aria-label':'Symbol'}):
            names.append(name.text)
        for price in listing.find_all('td', attrs={'aria-label':'Price (Intraday)'}):
            prices.append(price.text.replace(',', ''))
        for change in listing.find_all('td', attrs={'aria-label':'Change'}):
            changes.append(change.text)
        for volume in listing.find_all('td', attrs={'aria-label':'Volume'}):
            volumes.append(volume.text)
        id.append(index)
        index += 1

    data = {
        "id": id,
        "ticker": names,
        "price": prices,
        "change": changes,
        "volume": volumes
    }


    if url_index != 400:
        url_index += 100
    else:
        if METHOD == "POST":
            requests.post(url=API_ENDPOINT, data={"id": data["id"], "ticker": data["ticker"], "price": data["price"], "change": data["change"], "volume": data["volume"]})
            sys.exit()

        requests.put(url=API_ENDPOINT, data={"id": data["id"], "ticker": data["ticker"], "price": data["price"], "change": data["change"], "volume": data["volume"]})
        url_index = 0
        index = 0
        time.sleep(60)
