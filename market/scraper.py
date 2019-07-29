"""
Market scraper
"""
from bs4 import BeautifulSoup
from market.models import Market, Coin

MARKET_TABLE_ID = 'currencies-all'
COIN_TABLE_CLASS = 'cmc-cc-summary-table'


class MarketScraper(object):
    """ coinmarketcap.com scraper """

    def __init__(self, text):
        """
        Coin scraper
        :parse text: html text
        """
        self.text = text
        self.soup = BeautifulSoup(self.text, 'lxml')

    def _table(self, attrs):
        return self.soup.find('table', attrs=attrs)

    def scrape_market(self, limit=None):
        """
        scrapes all coins from coinmarketcap.com
        """
        coins = []
        for row in self._table({'id': MARKET_TABLE_ID}).find_all('tr')[1:]:
            tds = row.find_all('td')
            props = [td.get_text().strip() for td in tds]
            icon = tds[1].find('img')
            props.append(icon['src'] if icon else '')
            coins.append(Coin(**{
                'rank': props[0],
                'name': props[1].split('\n')[2],
                'symbol': props[2],
                'cap': props[3],
                'price': props[4],
                'supply': props[5].split('\n')[0],
                'volume': props[6],
                'percent1h': props[7],
                'percent24h': props[8],
                'percent7d': props[9]
            }))
            if limit and len(coins) == limit:
                break                
        return Market(coins)

    def _coin_val(self, rows, row_nbr, col=0, val=2):
        return rows[row_nbr].find_all('td')[col].get_text().split('\n')[val].strip()

    def scrape_coin(self):
        """
        scrapes single coin
        """
        details = self.soup.find('div', {'class': 'details-panel-item--name'})
        rows = self._table({'class': COIN_TABLE_CLASS}).find_all('tr')
        return Coin(**{
            'rank': self._coin_val(rows, 2, 0, 1).split('#')[1],
            'name': details.find_all('img')[0]['alt'],
            'symbol': details.find_all('span')[0].get_text()[1:-1],
            'cap': '${cap}'.format(cap=self._coin_val(rows, 3)),
            'price': '${price}'.format(price=self._coin_val(rows, 0)),
            'supply': self._coin_val(rows, 5),
            'volume': '${price}'.format(price=self._coin_val(rows, 4))})
