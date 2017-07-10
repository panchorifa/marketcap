"""
scraper tests
"""
from market.scraper import MarketScraper

PAGE = 'tests/samples/all.html'
text = open(PAGE).read()

def test_parser():
    market = MarketScraper(text).scrape()
    assert(len(market.coins) == 953)
    coin = market.coins[0]
    assert(int(coin.rank) == 1)
    assert(coin.icon == 'https://files.coinmarketcap.com/static/img/coins/16x16/bitcoin.png')
    assert(coin.symbol == 'BTC')
    assert(coin.name   == 'Bitcoin')
    assert(coin.price  == '$2499.55')
    assert(coin.cap    == '$41,077,509,717')
    assert(coin.volume == '$909,999,000')
    assert(coin.supply == '16,433,962')
    assert(coin.percent1h == '-0.59%')
    assert(coin.percent24h == '-3.91%')
    assert(coin.percent7d == '0.98%')

    coins = market.coins
    assert(coins[9].symbol == 'STRAT')
    assert(coins[10].symbol == 'EOS')

def test_limit():
    market = MarketScraper(text).scrape(5)
    assert(len(market.coins) == 5)
