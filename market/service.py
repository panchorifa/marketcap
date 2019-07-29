"""
Market Service
"""
import requests
from market.scraper import MarketScraper
from market.settings import MARKET_URL, COIN_URL, DEFAULT_COINS_LIMIT

class ServiceError(Exception):
    def __init__(self, status_code):
        self.status_code = status_code

def _get_url_content(url):
    res = requests.get(url)
    if res.status_code != 200:
        raise ServiceError(res.status_code)
    return res.text

class MarketService(object):
    """ Scraper facade """

    def __init__(self):
        """ Initializes service """
        self.api = requests

    def market(self, limit=DEFAULT_COINS_LIMIT):
        """ Returns all coins """
        text = _get_url_content(MARKET_URL)
        return MarketScraper(text).scrape_market(limit)

    def coin(self, name):
        """ Returns single coin """
        text = _get_url_content(COIN_URL.format(coin=name))
        return MarketScraper(text).scrape_coin()
