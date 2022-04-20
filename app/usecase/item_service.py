from abc import ABC, abstractmethod
from typing import Optional, List, cast

import shortuuid

from app.domain.item.item import Item
from app.domain.item.item_repository import ItemRepository


class ItemCommandUseCase(ABC):
    """ItemCommandUseCase defines an interface pattern."""

    item_repository: ItemRepository

    @abstractmethod
    def begin(self):
        raise NotImplementedError

    @abstractmethod
    def commit(self):
        raise NotImplementedError

    @abstractmethod
    def rollback(self):
        raise NotImplementedError


# class ItemQueryService(ABC):
#     """BookQueryService defines a query service inteface related Book entity."""
#
#     @abstractmethod
#     def find_by_id(self, id: str) -> Optional[Item]:
#         raise NotImplementedError
#
#     @abstractmethod
#     def find_all(self) -> List[Item]:
#         raise NotImplementedError


class ItemUseCase(ABC):
    def create_item(self, item: Item) -> Optional[Item]:
        raise NotImplementedError

    def fetch_item_by_id(self, id: str) -> Optional[Item]:
        raise NotImplementedError

    def fetch_items(self) -> List[Item]:
        raise NotImplementedError


class ItemUseCaseImpl(ItemUseCase):
    def __init__(self, item_command_use_case: ItemCommandUseCase):
        self.item_command_use_case: ItemCommandUseCase = item_command_use_case

    def create_item(self, item: Item) -> Optional[Item]:
        try:
            uuid = shortuuid.uuid()
            self.item_command_use_case.item_repository.create(item)
            self.item_command_use_case.commit()
            created_book = self.item_command_use_case.item_repository.find_by_id(uuid)
        except Exception:
            self.item_command_use_case.rollback()
            raise
        return cast(Item, created_book)

    def fetch_item_by_id(self, id: str) -> Optional[Item]:
        try:
            item = self.item_command_use_case.item_repository.find_by_id(id)
            if item is None:
                raise Exception("상품이 존재하지 않습니다.")
        except Exception:
            raise
        return item

    def fetch_items(self) -> List[Item]:
        try:
            items = self.item_command_use_case.item_repository.find_all()
        except Exception:
            raise
        return items
