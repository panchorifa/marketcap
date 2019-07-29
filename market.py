"""
Command line tool to scrape and parse coinmarketcap.com
"""
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
        'coins', help='List top 10 coins'
    )
    parser_market.add_argument(
        '-l', '--limit', type=int, required=False,
        help='Set the limit for top coins'
    )

    return parser_market

def _list(value):
    return [x.strip() for x in value.split(',')]

def main():
    parser, subparsers = create_main_parser()
    create_coins_parser(subparsers)

    args = parser.parse_args()

    if args.command == 'coins':
        try:
            print MarketService().market(args.limit or 10)
        except KeyboardInterrupt:
            pass

if __name__ == '__main__':
    main()
