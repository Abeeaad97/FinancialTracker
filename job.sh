#!/bin/bash

cd FinancialTracker/
pipenv run scrapy crawl indexes
pipenv run scrapy crawl stocks
