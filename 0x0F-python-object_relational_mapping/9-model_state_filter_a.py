#!/usr/bin/python3
"""
Listing all states  that contain letter a
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmake

if __name__ == "__main__":
    db_engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=db_engine)
    session = Session()
    Base.metadata.create_all()
    states = session.query(State).filter(State.name.like('%a\
            %')).order_by(State.id).all()
    for s in states:
        print("{}: {}".format(s.id, s.name))
    session.close()
