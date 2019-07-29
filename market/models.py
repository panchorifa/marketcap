"""
Market models
"""
import datetime

class Coin(object):
    """ Coin model """
    def __init__(self, **kwargs):
        self.rank = kwargs.pop('rank', None)
        self.name = kwargs.pop('name', None)
        self.symbol = kwargs.pop('symbol', None)
        self.cap = kwargs.pop('cap', None)
        self.price = kwargs.pop('price', None)
        self.supply = kwargs.pop('supply', None)
        self.volume = kwargs.pop('volume', None)
        self.percent1h = kwargs.pop('percent1h', None)
        self.percent24h = kwargs.pop('percent24h', None)
        self.percent7d = kwargs.pop('percent7d', None)

    def json(self):
        """ Returns map """
        return {
             'rank': self.rank,
             'name': self.name,
             'symbol': self.symbol,
              'cap': self.cap,
            'price': self.price,
           'supply': self.supply,
           'volume': self.volume}

    def __str__(self):
        return '{} {} {} {} {} {} {} {} {} {}'.format(
            self.rank.rjust(5),
            self.symbol.rjust(5),
            self.name.rjust(20),
            self.price.rjust(10),
            self.cap.rjust(18),
            self.volume.rjust(15),
            self.supply.rjust(18),
            self.percent1h.rjust(8) if self.percent1h else '',
            self.percent24h.rjust(8) if self.percent24h else '',
            self.percent7d.rjust(8) if self.percent7d else '')


class Market(object):
    """ Market model """
    def __init__(self, coins):
        self.coins = coins

    def json(self):
        """ Returns array of coins """
        return [c.json() for c in self.coins]

    def __str__(self):
        now = datetime.datetime.now()
        date = now.strftime('%b %d, %Y %H:%M:%S')
        print date
        print '='*125
        print '{} {} {} {} {} {} {} {} {}'.format(
                'rank'.rjust(11),
                'name'.rjust(20),
                'price'.rjust(10),
                'market cap'.rjust(18),
                'volume'.rjust(15),
                'supply'.rjust(18),
                '1h'.rjust(8),
                '24h'.rjust(8),
                '7d'.rjust(8))
        print '='*125
        for coin in sorted(self.coins, key=lambda x: int(x.rank)):
            print coin
            print '-'*125
        return date
