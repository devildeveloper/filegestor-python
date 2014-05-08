from sqlalchemy import Column, Date, DateTime,String, Integer, ForeignKey , func
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base=declarative_base()

class User(Base):
	__tablename__='user'
	id =Column(Integer,primary_key=True)
	name = Column(String(50))
	passw=Column(String(50))
	hired_on =Column(DateTime,default =func.now())
	status=Column(Integer,default=1)#0 = user disabled

class File(Base):
	__tablename__='file'
	id =Column(Integer,primary_key=True)
	created=Column(DateTime,default=func.now())
	name=Column(String(50))
	status=Column(Integer,default=1)
	expiration=Column(Date,default=func.now())
	user_id=Column(Integer,ForeignKey('user.id'))
	user =relationship(
		User,
		backref=backref('file',uselist=True,cascade='delete,all')
	)

from sqlalchemy import create_engine

#engine=create_engine('sqlite:///orm_in_detail.sqlite')
engine = create_engine('mysql://root:1234@127.0.0.1:3306/sqlalchemy', echo=False)
from sqlalchemy.orm import sessionmaker

session =sessionmaker()
session.configure(bind=engine)
Base.metadata.create_all(engine)