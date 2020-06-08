Scraper for coinmarketcap.com
=============================
Retrieves coins via:
1. cli (text)
2. http end point (json)


### Setup

	./install.sh


	installing lxml in ubuntu requires:

	"""
	sudo apt-get install libxml2-dev libxslt-dev
	sudo apt-get install python-lxml
	"""

### Running tests

```
pytest
```

### Running tests in watch mode

```
ptw
```

### Linting

```
pylint market
```

### Coverage

```
pytest-cov --cov=market
```


### Running CLI

```
python market.py coins -l 10 -f json > market-"$(date +"%b-%d-%y[%H:%M:%S]")".log
```

Generates text file. ie: market-Jul-07-17[16:29:44].log


### Running HTTP end point

```
python app.py

curl http://localhost:8000/market > market-"$(date +"%b-%d-%y[%H:%M:%S]")".json
curl http://localhost:8000/market?limit=5 > market-"$(date +"%b-%d-%y[%H:%M:%S]")".json
```

Generates json file. ie: market-Jul-07-17[16:29:44].json

```
{"market": [
{"name": "Bitcoin", "supply": "18,398,300 BTC", "price": "$9,695.32", "cap": "$178,377,380,011", "rank": "1", "volume": "$24,034,615,167", "symbol": "BTC"},
{"name": "Ethereum", "supply": "111,265,140 ETH", "price": "$241.90", "cap": "$26,914,755,808", "rank": "2", "volume": "$8,914,853,162", "symbol": "ETH"},
{"name": "Tether", "supply": "9,187,991,663 USDT *", "price": "$1.00", "cap": "$9,210,493,467", "rank": "3", "volume": "$27,396,609,573", "symbol": "USDT"},
{"name": "XRP", "supply": "44,112,853,111 XRP *", "price": "$0.202180", "cap": "$8,918,755,526", "rank": "4", "volume": "$1,088,395,137", "symbol": "XRP"},
{"name": "Bitcoin Cash", "supply": "18,429,363 BCH", "price": "$252.69", "cap": "$4,656,995,441", "rank": "5", "volume": "$1,878,843,688", "symbol": "BCH"},
{"name": "Bitcoin SV", "supply": "18,428,021 BSV", "price": "$191.41", "cap": "$3,527,321,681", "rank": "6", "volume": "$1,220,115,457", "symbol": "BSV"},
{"name": "Litecoin", "supply": "64,910,673 LTC", "price": "$46.23", "cap": "$3,000,703,580", "rank": "7", "volume": "$2,520,498,619", "symbol": "LTC"},
{"name": "Binance Coin", "supply": "155,536,713 BNB *", "price": "$17.37", "cap": "$2,702,104,483", "rank": "8", "volume": "$194,734,892", "symbol": "BNB"},
{"name": "EOS", "supply": "933,316,612 EOS *", "price": "$2.77", "cap": "$2,584,557,277", "rank": "9", "volume": "$1,841,381,675", "symbol": "EOS"},
{"name": "Cardano", "supply": "25,927,070,538 ADA", "price": "$0.085068", "cap": "$2,205,568,225", "rank": "10", "volume": "$237,969,209", "symbol": "ADA"}]}
```


### Serverless Deployment

```
zappa init
zappa deploy
```

### TODO

```
tox.ini
.travis.yml
```
