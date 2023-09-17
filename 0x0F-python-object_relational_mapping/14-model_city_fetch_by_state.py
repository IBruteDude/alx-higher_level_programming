#!/usr/bin/python3
''' Module demonstrating the use of the sqlalchemy database API '''
from sys import argv
from sqlalchemy.orm import Session, relationship
from sqlalchemy import create_engine
from model_state import State
from model_city import City

if __name__ == '__main__':
    host, port = "localhost", 3306
    user, password, database = argv[1], argv[2], argv[3]
    engine = create_engine(
        f"mysql://{user}:{password}@{host}:{port}/{database}"
    )
    session = Session(bind=engine)
    for state, city in session.query(State, City).filter(
            State.id == City.state_id).order_by(City.id).all():
        print(f"{state.name}: ({city.id}) {city.name}")
