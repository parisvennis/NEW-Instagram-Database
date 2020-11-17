import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    UserID = Column(Integer, primary_key=True)
    UserName = Column(String(250), nullable=False)
    FirstName = Column(String(250), nullable=False)
    LastName = Column(String(250), nullable=False)
    Email = Column(String(250), nullable=False)
    Password = Column(String(250), nullable=False)

class Post(Base):
    __tablename__ = 'post'
    PostID = Column(Integer, primary_key=True)
    UserID = Column(Integer, ForeignKey('user.UserID'))
    Description = Column(String(250), nullable=False)
    user = relationship(User)



# class Address(Base):
#     __tablename__ = 'address'
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')