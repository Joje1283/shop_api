import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database import Base

SQLALCHEMY_DATABASE_URL = "sqlite://"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
test_session = TestingSessionLocal()


@pytest.fixture(autouse=True)
def reset_test_db():
    # 테스트마다 DB스키마를 삭제 후 생성
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)
