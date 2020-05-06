import requests
from bs4 import BeautifulSoup
from celery import Celery
import pandas as pd
import json

app = Celery('tasks')


@app.task
def crawl_stocks():
    API_ENDPOINT = "http://localhost:8000/stocks/"
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
                return

            requests.put(url=API_ENDPOINT, json=json.dumps(stocks))
            return


def crawl_indices():
    API_ENDPOINT = "http://localhost:8000/indices/"
    METHOD = "PUT"

    # Data Table
    ids = []
    names = []
    prices = []
    changes = []
    percentChanges = []
    index = 0

    # URL to scrape data from
    IndicesUrl = "https://finance.yahoo.com/world-indices"

    # Send a GET request to retrieve html
    r = requests.get(IndicesUrl)
    data = r.text

    while True:
        # Load the data into soup
        soup = BeautifulSoup(data, 'lxml')

        for name in soup.find_all('td', attrs={'class':'data-col1'}):
            names.append(name.text)
        for price in soup.find_all('td', attrs={'class':'data-col2'}):
            prices.append(price.text.replace(',', ''))
        for change in soup.find_all('td', attrs={'class':'data-col3'}):
            changes.append(change.text.replace(',', ''))
        for percentChange in soup.find_all('td', attrs={'class':'data-col4'}):
            percentChanges.append(percentChange.text.replace(',', ''))
            ids.append(index)
            index += 1
        indices = {
            "id": ids,
            "name": names,
            "price": prices,
            "change": changes,
            "percentChange": percentChanges
        }

        if METHOD == "POST":
            requests.post(url=API_ENDPOINT, data=indices)
            return

        requests.put(url=API_ENDPOINT, data={"id": ids, "name": names, "price": prices, "change": changes, "percentChange": percentChanges})
        return

def crawl_crypto():
    API_ENDPOINT = "http://localhost:8000/crypto/"
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
                return

            requests.put(url=API_ENDPOINT, json=json.dumps(cryptos))
            return

while True:
    crawl_crypto()
    crawl_stocks()
    crawl_indices()
