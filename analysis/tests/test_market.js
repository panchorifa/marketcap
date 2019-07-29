const {latestMarket} = require('../src/market');

describe('coins cli', () => {
  test('find latest market', () => {
    const market = latestMarket(__dirname + '/markets/');
    const coins = market.market;
    expect(market.time).toBe('Jul-29-19[07:51:46]');
    expect(coins[0].name).toBe('Bitcoin');
    expect(coins[0].rank).toBe('1');
    expect(coins[0].symbol).toBe('BTC');
  });

  test('find latest market from invalid dir', () => {
    const market = () => {
      latestMarket(__dirname + '/invalid');
    };
    expect(market).toThrow();
  });

  // TODO define default dir in settings and
  // check here if that dir does exist
  test('find latest market from default dir', () => {
    const market = () => {
      latestMarket();
    };
    expect(market).toThrow();
  });

});
