from typing import Iterable

from .address import Address
from .orders import Order


class Member:
    def __init__(self, id: str, name: str, address: Address, orders: Iterable[Order]):
        self.id: str = id
        self.name: str = name
        self.address: Address = address
        self.orders = orders

    def __eq__(self, o: object) -> bool:
        if isinstance(o, Member):
            return self.id == o.id

        return False
