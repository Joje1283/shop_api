from __future__ import annotations

from enum import Enum
from datetime import datetime
from typing import Iterable
from typing import TYPE_CHECKING

from app.domain.entity import Entity

if TYPE_CHECKING:
    from app.domain.item.item import Item
    from app.domain.member.member import Member
    from app.domain.delivery import Delivery


class OrderItem(Entity):
    def __init__(self, id: int, item: Item, order: Order, order_price: int, count: int):
        self.id = id
        self.item = item
        self.order = order
        self.order_price = order_price
        self.count = count


class OrderStatus(Enum):
    ORDER = 1
    CANCEL = 2


class Order(Entity):
    def __init__(self, id: int, member: Member, order_items: Iterable[OrderItem],
                 delivery: Delivery, order_date: datetime, status: OrderStatus):
        self.id = id
        self.member = member
        self.order_items = order_items
        self.delivery = delivery
        self.order_date = order_date
        self.status = status
