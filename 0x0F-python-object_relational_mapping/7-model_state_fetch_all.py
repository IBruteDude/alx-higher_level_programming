#!/usr/bin/python3
''' Module demonstrating the use of the sqlalchemy database API '''
from sys import argv
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from model_state import State

if __name__ == '__main__':
    host, port = "localhost", 3306
    user, password, database = argv[1], argv[2], argv[3]
    engine = create_engine(
        f"mysql://{user}:{password}@{host}:{port}/{database}"
    )
    session = Session(bind=engine)
    for record in session.query(State).order_by(State.id).all():
        print(f"{record.id}: {record.name}")
