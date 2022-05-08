# Domain Layer

import enum

from sqlalchemy import Column, ForeignKey, Integer, String, Date, Table, Enum
from sqlalchemy.orm import relationship

from .database import Base


# table relation : https://docs.sqlalchemy.org/en/14/orm/basic_relationships.html#one-to-one
class Member(Base):
    __tablename__ = "member"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, unique=True)
    address = Column(String)
    orders = relationship("Order")  # 1:N with Order model


class Order(Base):
    class OrderStatus(enum.Enum):
        NONE = ""
        ORDER = "order"
        CANCEL = "cancel"

    __tablename__ = "order"

    id = Column(Integer, primary_key=True, index=True)
    member_id = Column(Integer, ForeignKey("member.id"))  # N:1 with Member model
    order_items = relationship("OrderItem")  # 1:N with OrderItem model
    delivery = relationship("Delivery", back_populates="order", uselist=False)  # 1:1 with Delivery model
    order_date = Column(Date(), index=True, nullable=False)
    status = Column(
        Enum(OrderStatus),
        nullable=False,
        default=OrderStatus.NONE,
    )


class Delivery(Base):
    class DeliveryStatus(enum.Enum):
        NONE = ""
        READY = "ready"
        COMP = "comp"

    __tablename__ = "delivery"

    id = Column(Integer, primary_key=True, index=True)
    parent_id = Column(Integer, ForeignKey('order.id'))  # 1:1 with Order model
    order = relationship("Order", back_populates="delivery")  # 1:1 with Order model
    address = Column(String)
    status = Column(
        Enum(DeliveryStatus),
        nullable=False,
        default=DeliveryStatus.NONE,
    )


class OrderItem(Base):
    __tablename__ = "order_item"

    id = Column(Integer, primary_key=True, index=True)
    item_id = Column(Integer, ForeignKey("item.id"))
    order_id = Column(Integer, ForeignKey("order.id"))
    order_price = Column(Integer, nullable=False)
    count = Column(Integer, nullable=False)


association_table = Table('category_item', Base.metadata,
                          Column('category_id', ForeignKey('category.id')),
                          Column('item_id', ForeignKey('item.id'))
                          )


class Item(Base):
    __tablename__ = "item"

    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    price = Column(Integer)
    stock_quantity = Column(Integer)
    categories = relationship("Category",
                              secondary=association_table)  # N:N with Catogory model
    dtype = Column(String)

    # Mapping Class Inheritance Hierarchies
    # https://docs.sqlalchemy.org/en/14/orm/inheritance.html#single-table-inheritance
    __mapper_args__ = {
        'polymorphic_on': dtype,
        'polymorphic_identity': 'item'
    }


class Album(Item):
    artist = Column(String(30))
    etc = Column(String)
    __mapper_args__ = {
        'polymorphic_identity': 'album'
    }


class Book(Item):
    author = Column(String)
    isbn = Column(String)
    __mapper_args__ = {
        'polymorphic_identity': 'book'
    }


class Movie(Item):
    director = Column(String)
    actor = Column(String)
    __mapper_args__ = {
        'polymorphic_identity': 'movie'
    }


class Category(Base):
    __tablename__ = "category"
    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    items = relationship("Item", secondary=association_table)

