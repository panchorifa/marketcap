import pytest
import json
import responses

from market.app import create_app
from market.service import MarketService
from market.settings import MARKET_URL, COIN_URL, DEFAULT_COINS_LIMIT

MARKET_RESPONSE = open('tests/samples/allsample.html', 'r').read()
COIN_RESPONSE = open('tests/samples/btc.html', 'r').read()

@pytest.fixture
def app(mocker):
    return create_app()

@responses.activate
def test_ping(client):
    responses.add(responses.GET, MARKET_URL, body=MARKET_RESPONSE, status=200)
    res = client.get('/ping')
    assert res.status_code == 200
    assert json.loads(res.data) == {'ping': 'pong'}

@responses.activate
def test_get_market(client):
    responses.add(responses.GET, MARKET_URL, body=MARKET_RESPONSE, status=200)
    res = client.get('/market')
    assert res.status_code == 200
    market = json.loads(res.data)

    assert len(market['market']) == DEFAULT_COINS_LIMIT
    assert market['market'][0]['name'] == 'Bitcoin'

@responses.activate
def test_get_top_coins(client):
    responses.add(responses.GET, MARKET_URL, body=MARKET_RESPONSE, status=200)
    res = client.get('/market?limit=3')
    assert res.status_code == 200
    market = json.loads(res.data)
    assert len(market['market']) == 3
    assert market['market'][0]['name'] == 'Bitcoin'

@responses.activate
def test_get_coin(client):
    responses.add(responses.GET, COIN_URL.format(coin='bitcoin'), body=COIN_RESPONSE, status=200)
    res = client.get('/coins/bitcoin')
    assert res.status_code == 200
    coin = json.loads(res.data)['coin']
    assert coin['symbol'] == 'BTC'
    assert coin['name'] == 'Bitcoin'

@responses.activate
def test_get_invalid_coin(client):
    responses.add(responses.GET, COIN_URL.format(coin='bitx'), body='', status=404)
    res = client.get('/coins/bitx')
    assert res.status_code == 404
