


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, DateTime, Enum, ARRAY, ForeignKey, Table
from sqlalchemy.orm import relationship, backref

from db import Base


class Option(Base):
  __tablename__ = 'options'

  color = Column(String)
  size = Column(Integer)
  stock = Column(Integer)

  product_id = Column(Integer, ForeignKey('products.id'))