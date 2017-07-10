"""
service tests
"""
from market.service import MarketService
from market.settings import MARKET_URL

from core import RequestMock

PAGE = 'tests/samples/all.html'
URLS = { MARKET_URL : PAGE }
service = MarketService(RequestMock(URLS))

def test_find_all():
    market = service.currentMarket()
    assert(len(market.coins) == 953)
    coins = market.coins
    assert(coins[9].symbol == 'STRAT')
    assert(coins[10].symbol == 'EOS')


def test_find_top_10():
    market = service.currentMarket(10)
    assert(len(market.coins) == 10)
