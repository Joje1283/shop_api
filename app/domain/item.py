from __future__ import annotations

from typing import List
from typing import TYPE_CHECKING

from .entity import Entity

if TYPE_CHECKING:
    from .category import Category


class Item(Entity):
    def __init__(self, id: int, name: str, price: int, stock_quantity: int, categories: List[Category]):
        self.id = id
        self.name = name
        self.price = price
        self.stock_quantity = stock_quantity
        self.categories = categories
