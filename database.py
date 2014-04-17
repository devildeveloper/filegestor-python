from sqlalchemy import Column, Date, String, Integer, ForeignKey , func
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

from datetime import date
Base=declarative_base()

class User(Base):
	__tablename__='user'
	id =Column(Integer,primary_key=True)
	name = Column(String)
	passw=Column(String)
	hired_on =Column(Date,default =func.now())
	status=Column(Integer,default=1)#0 = user disabled

class File(Base):
	__tablename__='file'
	id =Column(Integer,primary_key=True)
	name=Column(String)
	hired_on=Column(Date,default=func.now())
	expiration=Column(String)
	status=Column(Integer,default=1)#0 = user disabled	
	user_id=Column(Integer,ForeignKey('user.id'))
	user =relationship(
		User,
		backref=backref('file',uselist=True,cascade='delete,all')
	)

from sqlalchemy import create_engine

engine=create_engine('sqlite:///orm_in_detail.sqlite')

from sqlalchemy.orm import sessionmaker

session =sessionmaker()
session.configure(bind=engine)
Base.metadata.create_all(engine)