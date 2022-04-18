from __future__ import annotations

from typing import TYPE_CHECKING
from .entity import Entity

if TYPE_CHECKING:
    from .item import Item
    from .orders import Order


class OrderItem(Entity):
    def __init__(self, id: int, item: Item, order: Order, order_price: int, count: int):
        self.id = id
        self.item = item
        self.order = order
        self.order_price = order_price
        self.count = count
