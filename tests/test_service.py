"""
service tests
"""
import responses
from market.service import MarketService
from market.settings import MARKET_URL, COIN_URL

from core import RequestMock

service = MarketService()

MARKET_RESPONSE = open('tests/samples/allsample.html', 'r').read()
COIN_RESPONSE = open('tests/samples/btc.html', 'r').read()

@responses.activate
def test_market_with_default_limit():
    responses.add(responses.GET, MARKET_URL, body=MARKET_RESPONSE, status=200)
    market = service.market()
    assert len(market.coins) == 10
    coins = market.coins
    assert coins[8].symbol == 'BSV'
    assert coins[9].symbol == 'XLM'

@responses.activate
def test_market_top_3():
    responses.add(responses.GET, MARKET_URL, body=MARKET_RESPONSE, status=200)
    market = service.market(3)
    coins = market.coins
    assert len(coins) == 3
    assert coins[0].symbol == 'BTC'
    assert coins[1].symbol == 'ETH'
    assert coins[2].symbol == 'XRP'

@responses.activate
def test_coin():
    COIN = 'bitcoin'
    responses.add(responses.GET, COIN_URL.format(coin=COIN), body=COIN_RESPONSE, status=200)
    coin = service.coin(COIN)
    assert coin.name == 'Bitcoin'
    assert coin.symbol == 'BTC'
    assert coin.price == '$9503.61'
    assert coin.cap == '$169,591,156,093'
