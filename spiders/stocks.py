import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
import requests

API_ENDPOINT = "http://localhost:8000/stocks/"
API_KEY = "b*8p4e%!rk#hzm04$@j@6ie54&*wg+cpmmua0f_-(h4k(qpq0!"

# Data Table
names=[]
prices=[]
changes=[]
percentChanges=[]
marketCaps=[]
totalVolumes=[]
circulatingSupplys=[]

# URL to scrape data from
CryptoCurrenciesUrl = "https://finance.yahoo.com/currencies"

# Send a GET request to retrieve html
r = requests.get(CryptoCurrenciesUrl)
data = r.text

# Load the data into soup
soup = BeautifulSoup(data, 'lxml')

test = soup.find('tr', attrs={'data-reactid':40})
tName = test.find('td', attrs={'data-reactid':43})
tPrice = test.find('td', attrs={'data-reactid':44})
tChange = test.find('td', attrs={'data-reactid':45})
tPChange = test.find('td', attrs={'data-reactid':47})

test = tPrice.text.replace(',', '')
print(str(tName.text))
print(float(test))

params={
    "ticker":tName.text,
    "price":float(tPrice.text.replace(',', '')),
    "change":float(tChange.text.replace(',', '')),
    "percentChange":float(tPChange.text.replace(',', '').replace('%',''))
    }

r = requests.post(url=API_ENDPOINT, data=params)

# For Loop - Yahoo Finance requires us to crawl through data-id attributes
# the range was determined by their specific pattern of id increments
for index in range(40, 404, 14):
    # For Loop - grab each listing row and extract the data individually
    for listing in soup.find_all('tr', attrs={'data-reactid':index}):
        for name in listing.find_all('td', attrs={'data-reactid':index+3}):
            names.append(name.text)
        for price in listing.find_all('td', attrs={'data-reactid':index+4}):
            prices.append(price.text)
        for change in listing.find_all('td', attrs={'data-reactid':index+5}):
            changes.append(change.text)
        for percentChange in listing.find_all('td', attrs={'data-reactid':index+7}):
            percentChanges.append(percentChange.text)

# Create a dataframe with the pandas library to view results on Jupyter
pd.DataFrame({"Names": names, "Prices": prices, "Change": changes, "% Change": percentChanges})
