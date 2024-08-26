# test_portfolio.py

import unittest
from stock import Stock
from portfolio import Portfolio

class TestPortfolio(unittest.TestCase):
    def setUp(self):
        # Create instances of Stock for testing
        self.stock_a = Stock("UBER")
        self.stock_b = Stock("FINTUAL")

        # Set prices for different dates
        self.stock_a.set_price("2023-01-01", 30.0)
        self.stock_a.set_price("2024-01-01", 80.0)
        self.stock_b.set_price("2023-01-01", 2500.0)
        self.stock_b.set_price("2024-01-01", 3000.0)

        # Create a portfolio and add stocks
        self.portfolio = Portfolio()
        self.portfolio.add_stock(self.stock_a, 30.0)  # Purchased at 150
        self.portfolio.add_stock(self.stock_b, 2500.0)  # Purchased at 2500

    def test_profit_calculation(self):
        profit, annualized_return = self.portfolio.profit("2023-01-01", "2024-01-01")

        self.assertAlmostEqual(profit, 550.0)  # Profit calculation: (200 - 150) + (3000 - 2500)
        self.assertAlmostEqual(annualized_return, 0.2174, places=4) # Annualize return on 21.74%

    def test_price_not_available(self):
        # Test for price not available scenario
        with self.assertRaises(ValueError):
            self.portfolio.profit("2023-01-01", "2023-02-01")  # No price set for this date

    def test_same_start_end_date(self):
        # Test for same start and end date
        with self.assertRaises(ValueError):
            self.portfolio.profit("2024-01-01", "2024-01-01")

if __name__ == "__main__":
    unittest.main()
