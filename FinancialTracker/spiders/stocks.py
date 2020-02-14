import scrapy
import json
import loguru
from datetime import date
from lxml import etree
from FinancialTracker import items

# Spider to scrap Miscroft's historical data
class MSFT_Spider(scrapy.Spider):
    name = 'msft'
    allowed_domains = ["www.nasdaq.com"]

    # The url we are scraping
    start_url = {
        "https://www.nasdaq.com/market-activity/stocks/msft/historical"
    }

    # Parse the JSON data into the data model
    def parse(self, response):
        data_model = HistoricalData()

        # Process the webpage using etree
        data = etree.HTML(json.loads(response.body))

        # Locate data table
        hist_xpath = ".//tbody[@class=historical-data__table-body]"
        data_list = data.xpath(hist_xpath)

        # Load the data model
        data_model["DATE"] = data_list.xpath("./th[1]/text()")[0]
        data_model["CLOSE"] = data_list.xpath("./td[1]/text()")[0][1:]
        data_model["VOLUME"] = data_list.xpath("./td[2]/text()")[0]
        data_model["OPEN"] = data_list.xpath("./td[3]/text()")[0][1:]
        data_model["HIGH"] = data_list.xpath("./td[4]/text()")[0][1:]
        data_model["LOW"] = data_list.xpath("./td[5]/text()")[0][1:]

        yield data_model
