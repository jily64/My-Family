import enum

from sqlalchemy import create_engine, Column, Integer, String, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import datetime
from sqlalchemy import create_engine, Column, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import event

from pydantic import BaseModel

from typing import Optional


Base = declarative_base()

class TimestampMixin:
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    @classmethod
    def __declare_last__(cls):
        event.listen(cls, 'before_insert', TimestampMixin.before_insert)
        event.listen(cls, 'before_update', TimestampMixin.before_update)

    @staticmethod
    def before_insert(mapper, connection, target):
        now = datetime.datetime.now()
        target.created_at = now
        target.updated_at = now

    @staticmethod
    def before_update(mapper, connection, target):
        target.updated_at = datetime.datetime.now()

class Note(TimestampMixin, Base):
    __tablename__ = 'notes'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    
    
    def __repr__(self):
        return "<Note(username='%s', hashed_password='%s', role='%s', access_token='%s', refresh_token='%s')>" % (self.username, self.hashed_password, self.role, self.access_token, self.refresh_token)
    


if __name__ == "__main__":
    engine = create_engine('sqlite:///notes.db', echo=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()