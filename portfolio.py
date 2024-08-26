from typing import Dict, Tuple
from datetime import datetime
from stock import Stock


class Portfolio:
    def __init__(self) -> None:
        # Use a dictionary to store stocks and their prices
        self.stocks: Dict[Stock, float] = {}

    def add_stock(self, stock: Stock, price: float) -> None:
        # Add the stock with its price
        self.stocks[stock] = price

    def profit(self, start_date: str, end_date: str) -> Tuple[float, float]:
        total_start_value = 0.0
        total_end_value = 0.0

        for stock, purchase_price in self.stocks.items():
            start_price = stock.price(start_date)
            end_price = stock.price(end_date)

            if start_price is None or end_price is None:
                raise ValueError(f"Price not available for stock {stock.name} on the given dates.")

            # Calculate the value of the stock at the start and end dates
            total_start_value += purchase_price  # Assuming we consider the purchase price
            total_end_value += end_price  # The current price of the stock

        profit = total_end_value - total_start_value

        # Calculate annualized return
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")
        days_diff = (end - start).days

        if days_diff == 0:
            raise ValueError("Start date and end date cannot be the same.")

        annualized_return = ((total_end_value / total_start_value) ** (365 / days_diff)) - 1

        return profit, annualized_return
