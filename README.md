coinmarketcap.com scraper
=========================
retrieves the top 100 coins

## setup

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

Generates file with something like this: market-Jul-07-17[16:29:44].log

## Running flask to expose an HTTP end point with a json response

```
python app.py

curl http://localhost:8000/market > market-"$(date +"%b-%d-%y[%H:%M:%S]")".json
curl http://localhost:8000/market?limit=5 > market-"$(date +"%b-%d-%y[%H:%M:%S]")".json
```
