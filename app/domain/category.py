from __future__ import annotations

from typing import List
from typing import TYPE_CHECKING

from .entity import Entity

if TYPE_CHECKING:
    from .item import Item


class Category(Entity):
    def __init__(self, id: int, name: str, items: List[Item], parent: Category, child: List[Category]):
        self.id = id
        self.name = name
        self.items = items
        self.parent = parent
        self.child = child
