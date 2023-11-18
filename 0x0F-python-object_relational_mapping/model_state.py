#!/usr/bin/python3
"""creating model for state"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    State class that inherits from base class
    __tablename__(str): name of mysql table to store states
    id (sqlalchemy.Integer): The state's id
    name (sqlalchemy.String): name of state"""
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
