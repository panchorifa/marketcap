"""
scraper tests
"""
from market.scraper import MarketScraper

PAGE = 'tests/samples/page.html'
text = open(PAGE).read()

def test_parser():
    market = MarketScraper(text).scrape()
    assert(len(market.coins) == 100)
    coin = market.coins[0]
    assert(coin.name   == 'Bitcoin')
    assert(coin.price  == '$2542.40')
    assert(coin.cap    == '$41,780,370,229')
    assert(coin.volume == '$864,119,000')
    assert(coin.change == '-2.01%')
    assert(coin.supply == '16,433,437')

def test_limit():
    market = MarketScraper(text).scrape(5)
    assert(len(market.coins) == 5)
