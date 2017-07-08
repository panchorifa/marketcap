import unittest
# import os
import json
from market.app import app

class ApiTestCase(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client

    def test_get_all_coins(self):
        res = self.client().get('/market')
        self.assertEqual(res.status_code, 200)
        market = json.loads(res.data)
        self.assertEqual(len(market['market']), 100)
        self.assertEqual(market['market'][0]['name'], 'Bitcoin')

    def test_get_top_coins(self):
        res = self.client().get('/market?limit=3')
        self.assertEqual(res.status_code, 200)
        market = json.loads(res.data)
        self.assertEqual(len(market['market']), 3)
        self.assertEqual(market['market'][0]['name'], 'Bitcoin')

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
