from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, DateTime, Enum, ARRAY, ForeignKey, Table
from sqlalchemy.orm import relationship, backref

from db import Base


class Product(Base):
  __tablename__ = 'products'

  name = Column(String)
  provider = Column(String)
  price = Column(Integer)
