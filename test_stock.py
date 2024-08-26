# test_stock.py

import unittest
from stock import Stock

class TestStock(unittest.TestCase):
    def test_set_price(self):
        stock = Stock("UBER")
        stock.set_price("2023-01-01", 70.0)
        self.assertEqual(stock.price("2023-01-01"), 70.0)

    def test_price_not_set(self):
        stock = Stock("UBER")
        self.assertIsNone(stock.price("2023-01-01"))

if __name__ == "__main__":
    unittest.main()
