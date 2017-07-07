from bs4 import BeautifulSoup
from models import Market, Coin

class MarketScraper(object):
    def __init__(self, text):
        """
        Coin scraper
        :parse text: html text
        """
        self.text = text

    def scrape(self, limit=None):
        soup = BeautifulSoup(self.text, 'lxml')
        table = soup.find('table', attrs={'id': 'currencies'})
        coins = []
        for row in table.find_all('tr')[1:]:
            props = [td.get_text().strip() for td in row.find_all('td')]
            coins.append(Coin(props))
            if limit and len(coins) == limit:
                break
        return Market(coins)
