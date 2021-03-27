#!/usr/bin/python3
"""
adds the State object Louisiana to the database hbtn_0e_6_usa
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

    lou = State(name='Louisiana')
    session.add(lou)
    session.commit()

    print(lou.id)

    session.close()
