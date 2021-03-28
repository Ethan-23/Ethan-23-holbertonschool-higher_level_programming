#!/usr/bin/python3
"""
Thing
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, join

if __name__ == "__main__":
    engine_url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(sys.argv[1],
                                                                  sys.argv[2],
                                                                  sys.argv[3])
    states_eng = create_engine(engine_url)

    obj = sessionmaker(states_eng)
    session = obj()
    cities = session.query(State, City).join(City).order_by(City.id).all()

    for state, city in cities:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
