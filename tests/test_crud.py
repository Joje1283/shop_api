from sqlalchemy.orm import Session

from app.crud import Member
from app.schemas import MemberCreate
from tests.database import test_session, reset_test_db


class TestMember:
    def test_테스트(self, db: Session = test_session):
        pass