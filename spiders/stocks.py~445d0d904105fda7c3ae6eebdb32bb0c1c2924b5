import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd

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
df = pd.DataFrame({"Names": names, "Prices": prices, "Change": changes, "% Change": percentChanges})

# Export results to data.csv (Excel file)
df.to_csv(r'C:\Users\tyler\Documents\FinancialTracker\data.csv')
