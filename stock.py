from typing import Dict, Optional

class Stock:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.prices: Dict[str, float] = {}

    def set_price(self, date: str, price: float) -> None:
        self.prices[date] = price

    def get_price(self, date: str) -> Optional[float]:
        return self.prices.get(date)
