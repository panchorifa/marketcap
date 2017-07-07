import requests
from scraper import MarketScraper
from models import Market
from settings import MARKET_URL

class MarketService(object):
    def __init__(self, api=None):
        self.api = api if api else requests

    def currentMarket(self, limit=None):
        page = self.api.get(MARKET_URL)
        return MarketScraper(page.text).scrape(limit)
