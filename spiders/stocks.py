import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
import requests

API_ENDPOINT = "http://localhost:8000/indices/"
API_KEY = "b*8p4e%!rk#hzm04$@j@6ie54&*wg+cpmmua0f_-(h4k(qpq0!"

# Data Table
names=[]
prices=[]
changes=[]
volumes=[]

# URL to scrape data from
StocksUrl = "https://finance.yahoo.com/most-active?offset=0&count=100"

# Send a GET request to retrieve html
r = requests.get(StocksUrl)
data = r.text

# Load the data into soup
soup = BeautifulSoup(data, 'lxml')

for listing in soup.find_all('tr', attrs={'class':'simpTblRow'}):
    for name in listing.find_all('td', attrs={'aria-label':'Symbol'}):
      names.append(name.text)
    for price in listing.find_all('td', attrs={'aria-label':'Price (Intraday)'}):
      prices.append(price.text)
    for change in listing.find_all('td', attrs={'aria-label':'Change'}):
      changes.append(change.text)
    for volume in listing.find_all('td', attrs={'aria-label':'Volume'}):
      volumes.append(volume.text)

data = {
    "ticker": names,
    "price": prices,
    "change": changes,
    "volume": volumes
}

print(data["ticker"])
