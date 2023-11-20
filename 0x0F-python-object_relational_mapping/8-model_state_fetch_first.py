#!/usr/bin/python3
"""
Prints first state object from db
"""
from sys import argv as arg
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(arg[1], arg[1], arg[2]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)
    s = session.query(State).order_by(State.id).first()
    if s is None:
        print("Nothing")
    else:
        print("{}: {}".format(s.id, s.name))
