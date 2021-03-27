#!/usr/bin/python3
"""
prints all City objects from the database hbtn_0e_14_usa
"""
import sqlalchemy
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, db_name))
    Session = sessionmaker(bind=engine)
    session = Session()

    Base.metadata.create_all(engine)

    query = session.query(City, State).order_by(City.id).filter(
            City.state_id == State.id)
    for city, state in query:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.commit()

    session.close()
