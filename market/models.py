"""
market cap models
"""

# headings = ['rank', 'name', 'cap', 'price', 'supply', 'volume', 'change']

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
