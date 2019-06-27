from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, DateTime, Enum, ARRAY, ForeignKey, Table, Boolean
from sqlalchemy.orm import relationship, backref

from db import Base


class Product(Base):
  __tablename__ = 'products'

  name = Column(String)
  provider = Column(String)
  price = Column(Integer)
  options = relationship('Option', back_populates='product')

  shipping_price = Column(Integer)
  can_bundle = Column(Boolean)