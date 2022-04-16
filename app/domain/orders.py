from datetime import datetime
from typing import Iterable

from .entity import Entity
from .member import Member


class OrderItem(Entity):
    pass


class Delivery(Entity):
    pass


class OrderStatus(Entity):
    pass


class Order(Entity):
    def __init__(self, id: int, member: Member, order_items: Iterable[OrderItem],
                 delivery: Delivery, order_date: datetime, status: OrderStatus):
        self.id = id
        self.member = member
        self.order_items = order_items
        self.delivery = delivery
        self.order_date = order_date
        self.status = status
