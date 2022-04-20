from abc import ABC, abstractmethod
from typing import Optional, List, cast

import shortuuid

from app.domain.order.order import Order
from app.domain.order.order_repository import OrderRepository


class OrderCommandUseCase(ABC):
    order_repository: OrderRepository

    @abstractmethod
    def begin(self):
        raise NotImplementedError

    @abstractmethod
    def commit(self):
        raise NotImplementedError

    @abstractmethod
    def rollback(self):
        raise NotImplementedError


class OrderUseCase(ABC):
    def create_order(self, item: Order) -> Optional[Order]:
        raise NotImplementedError

    def fetch_order_by_id(self, id: str) -> Optional[Order]:
        raise NotImplementedError


class OrderUseCaseImpl(OrderUseCase):
    def __init__(self, order_commnad_usecase: OrderCommandUseCase):
        self.order_command_usecase: OrderCommandUseCase = order_commnad_usecase

    def create_order(self, item: Order) -> Optional[Order]:
        try:
            uuid = shortuuid.uuid()
            self.order_command_usecase.order_repository.create(item)
            self.order_command_usecase.commit()
            created_book = self.order_command_usecase.order_repository.find_by_id(uuid)
        except Exception:
            self.order_command_usecase.rollback()
            raise
        return cast(Order, created_book)

    def fetch_order_by_id(self, id: str) -> Optional[Order]:
        try:
            order = self.order_command_usecase.order_repository.find_by_id(id)
            if order is None:
                raise Exception("상품이 존재하지 않습니다.")
        except Exception:
            raise
        return order
