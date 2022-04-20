from abc import ABC, abstractmethod
from typing import Optional, List, cast

import shortuuid

from app.domain.member.member import Member
from app.domain.member.member_repository import MemberRepository


class MemberCommandUseCase(ABC):
    member_repository: MemberRepository

    @abstractmethod
    def begin(self):
        raise NotImplementedError

    @abstractmethod
    def commit(self):
        raise NotImplementedError

    @abstractmethod
    def rollback(self):
        raise NotImplementedError


class MemberUseCase(ABC):
    def create_member(self, item: Member) -> Optional[Member]:
        raise NotImplementedError

    def fetch_member_by_id(self, id: str) -> Optional[Member]:
        raise NotImplementedError

    def fetch_member_by_name(self, name: str) -> Optional[Member]:
        raise NotImplementedError

    def fetch_members(self) -> List[Member]:
        raise NotImplementedError


class ItemUserCaseImpl(MemberUseCase):
    def __init__(self, member_command_usecase: MemberCommandUseCase):
        self.member_command_usecase: MemberCommandUseCase = member_command_usecase

    def create_member(self, item: Member) -> Optional[Member]:
        try:
            uuid = shortuuid.uuid()
            self.member_command_usecase.member_repository.create(item)
            self.member_command_usecase.commit()
            created_book = self.member_command_usecase.member_repository.find_by_id(uuid)
        except Exception:
            self.member_command_usecase.rollback()
            raise
        return cast(Member, created_book)

    def fetch_member_by_id(self, id: str) -> Optional[Member]:
        try:
            member = self.member_command_usecase.member_repository.find_by_id(id)
            if member is None:
                raise Exception("상품이 존재하지 않습니다.")
        except Exception:
            raise
        return member

    def fetch_member_by_name(self, name: str) -> Optional[Member]:
        try:
            member = self.member_command_usecase.member_repository.find_by_name(name)
            if member is None:
                raise Exception("상품이 존재하지 않습니다.")
        except Exception:
            raise
        return member

    def fetch_members(self) -> List[Member]:
        try:
            members = self.member_command_usecase.member_repository.find_all()
        except Exception:
            raise
        return members
