from tax_calculator import TaxCalculator
from item import Item


class Order:
    def __init__(self, country: str):
        self.country = country
        self.items: list[Item] = []

    def add_item(self, item: Item):
        self.items.append(item)

    def get_total(self) -> float:
        total = 0.0
        for item in self.items:
            total += item.price * item.quantity

        tax_calculator = TaxCalculator(self.country)
        total += tax_calculator.get_taxes(total)
        return total
