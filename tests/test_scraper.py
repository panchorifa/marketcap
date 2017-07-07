"""
scraper tests
"""
from market.scraper import MarketScraper

PAGE = 'tests/samples/page.html'

def test_parser():
    text = open(PAGE).read()
    market = MarketScraper(text).scrape()
    coin = market.coins[0]
    assert(coin.name == 'Bitcoin')
    assert(coin.price == '$2542.40')
    assert(coin.cap == '$41,780,370,229')
    assert(coin.volume == '$864,119,000')
    assert(coin.change == '-2.01%')
    assert(coin.supply == '16,433,437')
