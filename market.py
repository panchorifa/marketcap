"""
Command line tool to scrape and parse coinmarketcap.com
"""
import json
import requests
import argparse
from market.service import MarketService

def create_main_parser():
    parser = argparse.ArgumentParser(
        description='List top 100 crypto coins',
        prog='marketcap'
    )
    subparsers = parser.add_subparsers(
        title='commands',
        help='valid commands',
        dest='command'
    )
    return parser, subparsers

def create_coins_parser(subparsers):
    parser_market = subparsers.add_parser(
        'coins', help='List top 100 coins'
    )
    parser_market.add_argument(
        '-l', '--limit', type=int, required=False,
        help='Set the limit for top coins; 0 to get all.'
    )
    parser_market.add_argument(
        '-f', '--format', type=str, required=False,
        help='Request supported formats: json'
    )

    return parser_market

def _list(value):
    return [x.strip() for x in value.split(',')]

def jsonify(market):
    res = '{"market": [\n'
    for i, coin in enumerate(market.coins):
        if i > 0:
            res += ',\n'
        res += '{}'.format(json.dumps(coin.json()))
    res += ']}'
    return res

def main():
    parser, subparsers = create_main_parser()
    create_coins_parser(subparsers)

    args = parser.parse_args()

    if args.command == 'coins':
        try:
            limit = 100 if args.limit is None else args.limit
            market = MarketService().market(limit)
            if args.format == 'json':
                print jsonify(market)
            else:
                print market
        except KeyboardInterrupt:
            pass

if __name__ == '__main__':
    main()
