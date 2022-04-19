from abc import ABC, abstractmethod
from typing import Optional

from app.domain.order.order import Order


class ItemRepository(ABC):
    """ItemRepository defines a repository interface for Item entity."""

    @abstractmethod
    def create(self, item: Order) -> Optional[Order]:
        raise NotImplementedError

    @abstractmethod
    def find_by_id(self, id: int) -> Optional[Order]:
        raise NotImplementedError
