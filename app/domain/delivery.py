from __future__ import annotations

from enum import Enum
from typing import TYPE_CHECKING

from .entity import Entity

if TYPE_CHECKING:
    from .address import Address
    from app.domain.order.orders import Order


class DeliveryStatus(Enum):
    READY = 'ready'
    COMP = 'comp'


class Delivery(Entity):
    def __init__(self, id: int, order: Order, address: Address, status: DeliveryStatus):
        self.id = id
        self.order = order
        self.address = address
        self.status = status
