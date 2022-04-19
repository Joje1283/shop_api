from abc import ABC, abstractmethod
from typing import List, Optional

from app.domain.member.member import Member


class MemberRepository:
    """BookRepository defines a repository interface for Book entity."""

    @abstractmethod
    def create(self, member: Member) -> Optional[Member]:
        raise NotImplementedError

    @abstractmethod
    def find_by_id(self, id: str) -> Optional[Member]:
        raise NotImplementedError

    @abstractmethod
    def find_by_name(self, name: str) -> Optional[Member]:
        raise NotImplementedError

    @abstractmethod
    def update(self, member: Member) -> Optional[Member]:
        raise NotImplementedError

    @abstractmethod
    def find_all(self) -> Optional[List[Member]]:
        raise NotImplementedError

