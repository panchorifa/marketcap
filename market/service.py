from scraper import MarketScraper
from models import Market
from settings import MARKET_URL

class MarketService(object):
    def __init__(self, api):
        self.api = api

    def currentMarket(self):
        page = self.api.get(MARKET_URL)
        return MarketScraper(page).scrape()
