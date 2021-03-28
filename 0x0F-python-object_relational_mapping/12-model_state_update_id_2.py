#!/usr/bin/python3
"""
Thing
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine_url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(sys.argv[1],
                                                                  sys.argv[2],
                                                                  sys.argv[3])
    states_eng = create_engine(engine_url)

    obj = sessionmaker(states_eng)
    session = obj()

    replace = session.query(State).filter_by(id=2).first()
    replace.name = "New Mexico"
    session.commit()
    session.close()
