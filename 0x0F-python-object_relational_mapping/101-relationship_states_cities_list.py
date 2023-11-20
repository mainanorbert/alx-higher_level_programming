#!/usr/bin/python3
""" Listing states corresponsing to cities
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)

    for s in session.query(State).order_by(State.id):
        print("{}: {}".format(s.id, s.name))
        for c in s.cities:
            print("  {}: {}".format(c.id, c.name))
