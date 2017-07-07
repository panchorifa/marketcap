"""
market cap models
"""
import datetime

class Coin(object):
    def __init__(self, props):
        self.rank = props[0]
        self.name = props[1]
        self.cap = props[2]
        self.price = props[3]
        self.supply = props[4].split('\n')[0]
        self.volume = props[5]
        self.change = props[6]

    def __str__(self):
        return '{} {} {} {} {} {}'.format(
                self.name.rjust(20),
                self.price.rjust(10),
                self.cap.rjust(18),
                self.volume.rjust(15),
                self.change.rjust(8),
                self.supply.rjust(18))


class Market(object):
    def __init__(self, coins):
        self.coins = coins

    def __str__(self):
        now = datetime.datetime.now()
        date = now.strftime('%b %d, %Y %H:%M:%S')
        print date
        print '{} {} {} {} {} {}'.format(
                'name'.rjust(20),
                'price'.rjust(10),
                'market cap'.rjust(18),
                'volume'.rjust(15),
                'change'.rjust(8),
                'supply'.rjust(18))
        for coin in self.coins:
            print coin
            print '-'*100
        return date
