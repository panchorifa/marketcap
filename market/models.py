"""
market cap models
"""
import datetime


class Coin(object):
    def __init__(self, props):
        self.rank = props[0]
        self.name = props[1]
        self.symbol = props[2]
        self.cap = props[3]
        self.price = props[4]
        self.supply = props[5].split('\n')[0]
        self.volume = props[6]
        self.percent1h = props[7]
        self.percent24h = props[8]
        self.percent7d = props[9]
        self.icon = props[10]

    def json(self):
        return {
             'rank': self.rank,
             'name': self.name,
             'symbol': self.symbol,
              'cap': self.cap,
            'price': self.price,
           'supply': self.supply,
           'volume': self.volume,
           'percent1h': self.percent1h,
           'percent24h': self.percent24h,
           'percent7d': self.percent7d,
           'icon': self.icon}

    def __str__(self):
        return '{} {} {} {} {} {} {} {} {} {}'.format(
                self.rank.rjust(5),
                self.symbol.rjust(5),
                self.name.rjust(20),
                self.price.rjust(10),
                self.cap.rjust(18),
                self.volume.rjust(15),
                self.supply.rjust(18),
                self.percent1h.rjust(8),
                self.percent24h.rjust(8),
                self.percent7d.rjust(8))


class Market(object):
    def __init__(self, coins):
        self.coins = coins

    def json(self):
        return [c.json() for c in self.coins]

    def __str__(self):
        now = datetime.datetime.now()
        date = now.strftime('%b %d, %Y %H:%M:%S')
        print date
        print '='*100
        print '{} {} {} {} {} {} {}'.format(
                'rank'.rjust(5),
                'name'.rjust(20),
                'price'.rjust(10),
                'market cap'.rjust(18),
                'volume'.rjust(15),
                'change'.rjust(8),
                'supply'.rjust(18))
        print '='*100
        for coin in self.coins.sort(key=lambda x: x.rank):
            print coin
            print '-'*100
        return date
