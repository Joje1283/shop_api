from abc import ABC, abstractmethod
from typing import Optional

from app.domain.item.item import Item


class ItemRepository(ABC):
    """ItemRepository defines a repository interface for Item entity."""

    @abstractmethod
    def create(self, item: Item) -> Optional[Item]:
        raise NotImplementedError

    @abstractmethod
    def find_by_id(self, id: str) -> Optional[Item]:
        raise NotImplementedError

    @abstractmethod
    def update(self, item: Item) -> Optional[Item]:
        raise NotImplementedError
