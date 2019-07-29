"""
scraper tests
"""
from market.scraper import MarketScraper

MARKET_TEXT = open('tests/samples/allsample.html').read()
COIN_TEXT = open('tests/samples/btc.html').read()

def test_scrape_market():
    market = MarketScraper(MARKET_TEXT).scrape_market()
    assert(len(market.coins) == 11)
    btc = market.coins[0]
    assert int(btc.rank) == 1
    assert btc.symbol == 'BTC'
    assert btc.name   == 'Bitcoin'
    assert btc.price  == '$9780.51'
    assert btc.cap    == '$174,469,078,645'
    assert btc.volume == '$14,933,437,287'
    assert btc.supply == '17,838,437'
    assert btc.percent1h == '0.38%'
    assert btc.percent24h == '-3.12%'
    assert btc.percent7d == '-6.79%'

    coins = market.coins
    assert coins[1].symbol == 'ETH'
    assert coins[2].symbol == 'XRP'
    assert coins[3].symbol == 'LTC'
    assert coins[4].symbol == 'BCH'
    assert coins[5].symbol == 'BNB'
    assert coins[6].symbol == 'EOS'
    assert coins[7].symbol == 'USDT'
    assert coins[8].symbol == 'BSV'
    assert coins[9].symbol == 'XLM'
    assert coins[10].symbol == 'BCD'

def test_scrape_market_top_5():
    market = MarketScraper(MARKET_TEXT).scrape_market(5)
    assert len(market.coins) == 5

def test_scrape_coin():
    coin = MarketScraper(COIN_TEXT).scrape_coin()
    assert coin.symbol == 'BTC'
    assert coin.name == 'Bitcoin'
    assert coin.rank == '1'
    assert coin.cap == '$169,591,156,093'
    assert coin.price == '$9503.61'
    assert coin.supply == '17,844,912'
    assert coin.volume == '$14,795,854,714'
