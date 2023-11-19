#!/usr/bin/python3

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}\
            ".format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)
    # states = session.query(State).order_by(State.id)
    for s in session.query(State).order_by(State.id):
        print("{}: {}".format(s.id, s.id))
