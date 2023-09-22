#!/usr/bin/python3
''' Module defining the sql tabled model of the City class '''
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.schema import ForeignKey

Base = declarative_base()


class City(Base):
    ''' The declarative representation of the City class table '''
    __tablename__ = 'cities'
    id = Column(Integer, nullable=False, unique=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"))
