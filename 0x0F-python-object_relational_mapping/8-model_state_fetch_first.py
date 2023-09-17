#!/usr/bin/python3
from sys import argv
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from model_state import State

if __name__ == '__main__':
    host, user, password, database, port = "localhost", argv[1], argv[2], argv[3], 3306
    engine = create_engine(f"mysql://{user}:{password}@{host}:{port}/{database}")
    session = Session(bind=engine)
    record = session.query(State).first()
    if record is None:
        print("Nothing")
    else:
        print(f"{record.id}: {record.name}")
