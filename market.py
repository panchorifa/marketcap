"""
Command line tool to scrape and parse craigslist cities
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
        'coins', help='List top 100 coins'
    )
    parser_market.add_argument(
        '-l', '--limit', type=int, required=True,
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
            service = MarketService(requests)
            print service.currentMarket(args.limit)
        except KeyboardInterrupt:
            pass

if __name__ == '__main__':
    main()
