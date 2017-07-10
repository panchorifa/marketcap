from bs4 import BeautifulSoup
from models import Market, Coin

TABLE_ID = 'currencies-all'

class MarketScraper(object):
    def __init__(self, text):
        """
        Coin scraper
        :parse text: html text
        """
        self.text = text

    def scrape(self, limit=None):
        soup = BeautifulSoup(self.text, 'lxml')
        table = soup.find('table', attrs={'id': TABLE_ID})
        coins = []
        for row in table.find_all('tr')[1:]:
            tds = row.find_all('td')
            props = [td.get_text().strip() for td in tds]
            icon = tds[1].find('img')
            props.append(icon['src'] if icon else '')
            coins.append(Coin(props))
            if limit and len(coins) == limit:
                break
        return Market(coins)
