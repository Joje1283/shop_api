from sqlalchemy.orm import Session

from app.crud import Member
from app.schemas import MemberCreate
from tests.database import test_session


class TestMember:
    def test_회원가입(self, db: Session = test_session):
        # given
        member_create = MemberCreate(name="조재식")
        # when
        member = Member.create_member(db, member_create)
        # then
        assert member.name == "조재식"

    def test_중복회원제외(self, db: Session = test_session):
        pass