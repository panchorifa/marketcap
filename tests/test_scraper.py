"""
scraper tests
"""
from market.scraper import MarketScraper

MARKET_TEXT = open('tests/samples/allsample.html').read()
COIN_TEXT = open('tests/samples/btc.html').read()

def test_scrape_market_with_default_limit():
    market = MarketScraper(MARKET_TEXT).scrape_market()
    assert(len(market.coins) == 11)
    btc = market.coins[0]
    assert int(btc.rank) == 1
    assert btc.symbol == 'BTC'
    assert btc.name   == 'Bitcoin'
    assert btc.price  == '$9,701.35'
    assert btc.cap    == '$178,487,831,257'
    assert btc.volume == '$24,160,676,973'
    assert btc.supply == '18,398,250'
    assert btc.percent1h == '-0.37%'
    assert btc.percent24h == '2.11%'
    assert btc.percent7d == '1.46%'

    coins = market.coins
    assert coins[1].symbol == 'ETH'
    assert coins[2].symbol == 'USDT'
    assert coins[3].symbol == 'XRP'
    assert coins[4].symbol == 'BCH'
    assert coins[5].symbol == 'BSV'
    assert coins[6].symbol == 'LTC'
    assert coins[7].symbol == 'BNB'
    assert coins[8].symbol == 'EOS'
    assert coins[9].symbol == 'ADA'
    assert coins[10].symbol == 'XTZ'

def test_scrape_market_with_invalid_limit():
    market = MarketScraper(MARKET_TEXT).scrape_market(-1)
    assert market.coins == []

def test_scrape_market_with_limit():
    market = MarketScraper(MARKET_TEXT).scrape_market(2)
    assert len(market.coins) == 2

def test_scrape_coin():
    coin = MarketScraper(COIN_TEXT).scrape_coin()
    assert coin.symbol == 'BTC'
    assert coin.name == 'Bitcoin'
    assert coin.rank == '1'
    assert coin.cap == '$169,591,156,093'
    assert coin.price == '$9503.61'
    assert coin.supply == '17,844,912'
    assert coin.volume == '$14,795,854,714'
