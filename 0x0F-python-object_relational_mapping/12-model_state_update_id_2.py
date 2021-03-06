#!/usr/bin/python3
"""Function to print states in asc order"""


from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker()
    session = Session(bind=engine)

    state = session.query(State).get(2)
    state.name = 'New Mexico'
    session.add(state)
    session.commit()
    session.close()
