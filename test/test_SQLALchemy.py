# encoding: utf-8

"""

@author: kevin

@contact: kevin_678@126.com


@file: test_SQLALchemy.py

@time: 2018/4/28 17:59

@desc:

"""

import sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = sqlalchemy.create_engine('sqlite:///:memory:', echo=True)

Base = declarative_base()

Session = sessionmaker(bind=engine)

session = Session()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    fullname = Column(String(50))
    password = Column(String(50))

    def __repr__(self):
        return "<User(name='%s', fullname='%s', password='%s')>" % (
            self.name, self.fullname, self.password)


if __name__ == '__main__':
    print User.__table__

    Base.metadata.create_all(engine)

    session.add_all(
        [
            User(name="test", fullname="ttt", password="ttt"),
            User(name="test1", fullname="ttt1", password="ttt1")
        ]
    )

    tmp = User(name="test")

    users = session.query(User).filter_by(name="test")

    for user in users:
        print user
