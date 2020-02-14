# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

# Test model for NASDAQ Historical Data
class HistoricalData(scrapy.Item):
    date = scrapy.Field()
    close = scrapy.Field()
    volume = scrapy.Field()
    open = scrapy.Field()
    high = scrapy.Field()
    low = scrapy.Field()
