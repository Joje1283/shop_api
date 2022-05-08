from sqlalchemy.orm import Session
from tests.database import test_session


class TestMember:
    def test_테스트(self, db: Session = test_session):
        pass

