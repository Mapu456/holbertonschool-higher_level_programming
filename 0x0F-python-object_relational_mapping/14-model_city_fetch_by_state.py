#!/usr/bin/python3
"""Function to print states in asc order"""


from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker()
    session = Session(bind=engine)

    tables = session.query(State, City).join(City).all()
    for state, city in tables:
        print('{}: ({}) {}'.format(state.name, city.id, city.name))
    session.close()
