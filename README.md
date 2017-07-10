Scraper for coinmarketcap.com
=============================
Retrieves the top 100 coins via:
1. cli (text)
2. http end point(json)


### Setup

	pip install -r requirements.txt;pip install -r requirements_dev.txt;


	installing lxml in ubuntu requires:

	"""
	sudo apt-get install libxml2-dev libxslt-dev
	sudo apt-get install python-lxml
	"""

### Testing

```
nosetests -c .noserc_local
```

Then check `test_results/coverage/index.html` for the HTML report.


### Running CLI

```
python market.py coins > market-"$(date +"%b-%d-%y[%H:%M:%S]")".log
```

Generates text file. ie: market-Jul-07-17[16:29:44].log


### Running Flask

```
python app.py

curl http://localhost:8000/market > market-"$(date +"%b-%d-%y[%H:%M:%S]")".json
curl http://localhost:8000/market?limit=5 > market-"$(date +"%b-%d-%y[%H:%M:%S]")".json
```

Generates json file. ie: market-Jul-07-17[16:29:44].json


### Serverless Deployment

```
zappa init
zappa deploy
```
