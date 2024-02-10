# SQLAlchemy Models
# Purpose: SQLAlchemy models are used for defining the structure of your database tables.
# They are essentially a part of the ORM (Object-Relational Mapping) layer that maps Python classes to database tables, 
# allowing for easy querying and manipulation of database data using Python code.

# Database Interaction: These models are directly linked to your database. 
# They define the schema of your database with columns, data types, relationships, constraints, and more.

# Usage: You use SQLAlchemy models to perform CRUD (Create, Read, Update, Delete) operations directly on your database. 
# They're essential for database migrations and schema management.

# Dependency: SQLAlchemy is a database toolkit and ORM for Python, so these models are specific to SQLAlchemy and are used in conjunction with its API.

from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base

class Store(Base):
    __tablename__ = 'stores'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    balance = Column(Float, default=0.0)
    is_open = Column(Boolean, default=True)
    inventory = relationship("Item", back_populates="store")

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Float)
    store_id = Column(Integer, ForeignKey('stores.id'))
    store = relationship("Store")
    store = relationship("Store", back_populates="inventory")
