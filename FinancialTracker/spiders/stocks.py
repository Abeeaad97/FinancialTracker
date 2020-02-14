import scrapy
import json
import loguru
import items
from datetime import date
from lxml import etree

# Spider to scrap Miscroft's historical data
class MSFT_Spider(scrapy.Spider):
    name = 'stocks'
    allowed_domains = ["www.nasdaq.com"]

    # The url we are scraping
    start_url = {
        "https://www.nasdaq.com/market-activity/stocks/msft/historical"
    }

    # Parse the JSON data into the data model
    def parse(self, response):
        data_model = HistoricalData()

        for index in json.loads(response.body):
            # Process the webpage using etree
            data = etree.HTML(i)

            # Locate data table
            hist_xpath = ".//tbody[@class=historical-data__table-body]"
            data_list = data.xpath(hist_xpath)

            for i in data_list:
                # Load the data model
                data_model["DATE"] = i.xpath("./th[1]/text()")[0]
                data_model["CLOSE"] = i.xpath("./td[1]/text()")[0][1:]
                data_model["VOLUME"] = i.xpath("./td[2]/text()")[0]
                data_model["OPEN"] = i.xpath("./td[3]/text()")[0][1:]
                data_model["HIGH"] = i.xpath("./td[4]/text()")[0][1:]
                data_model["LOW"] = i.xpath("./td[5]/text()")[0][1:]

                yield data_model
