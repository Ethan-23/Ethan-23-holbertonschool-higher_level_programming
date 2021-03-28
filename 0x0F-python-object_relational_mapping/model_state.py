#!/usr/bin/python3
"""
Things
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class State(Base):
    """State Class"""
    __tablename__ = 'states'
    id = Column('id', Integer, primary_key=True, nullable=False)
    name = Column('name', String(128), nullable=False)
