#!/usr/bin/python3
"""creating model for state"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    Inheriting a base class
    __tablename__(str): name of mysql table to store states
    id (sqlalchemy.Integer): The state's id
    name (sqlalchemy.string): name of state"""
    __tablename__ = "states"
    id = column(Integer, primary_key=True)
    name = column(String(128), nullable=False)
