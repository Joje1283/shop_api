# Service Layer
from sqlalchemy.orm import Session
from . import models, schemas


class Member:
    # Todo: Repository 레이어 분리
    @staticmethod
    def get_member(db: Session, member_id: int):
        return db.query(models.Member).filter(models.Member.id == member_id).first()

    @staticmethod
    def get_member_by_name(db: Session, name: str):
        return db.query(models.Member).filter(models.Member.email == name).first()

    @staticmethod
    def get_members(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.Member).offset(skip).limit(limit).all()

    @staticmethod
    def create_member(db: Session, member: schemas.MemberCreate):
        # fake_hashed_password = member.password + "notreallyhashed"
        db_member = models.Member(name=member.name)
        db.add(db_member)
        db.commit()
        db.refresh(db_member)
        return db_member

    @staticmethod
    def get_items(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.Item).offset(skip).limit(limit).all()


class Item:
    pass


class Order:
    pass
