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
});
