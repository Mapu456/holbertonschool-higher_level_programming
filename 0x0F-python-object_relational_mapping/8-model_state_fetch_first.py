#!/usr/bin/python3
"""Function to print states in asc order"""


from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Session = sessionmaker()
    session = Session(bind=engine)

    query = session.query(State).where(State.name == 'California')

    for item in query:
        print("{}: {}".format(item.id, item.name))