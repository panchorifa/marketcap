#!/bin/sh
python market.py coins -l 0 -f json | python -mjson.tool > data/market-"$(date +"%b-%d-%y[%H:%M:%S]")".json
