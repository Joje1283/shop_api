# Presentation Layer
from pydantic import BaseModel


class Member(BaseModel):
    name: str
    address: str | None = ''

    class Config:
        orm_mode = True


class MemberCreate(Member):
    pass
