from __future__ import annotations

from typing import Iterable
from typing import TYPE_CHECKING
from .entity import Entity

if TYPE_CHECKING:
    from .orders import Order
    from .address import Address


class Member(Entity):
    def __init__(self, id: str, name: str, address: Address, orders: Iterable[Order]):
        self.id: str = id
        self.name: str = name
        self.address: Address = address
        self.orders = orders
