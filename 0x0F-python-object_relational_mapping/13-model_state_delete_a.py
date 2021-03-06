#!/usr/bin/python3
"""
deletes all State objects with a name containing the
letter a from the database hbtn_0e_6_usa
"""
import sqlalchemy
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, db_name))
    Session = sessionmaker(bind=engine)
    session = Session()

    Base.metadata.create_all(engine)

    state = session.query(State).filter(State.name.like('%a%')).all()
    for s in state:
        session.delete(s)
    session.commit()

    session.close()
