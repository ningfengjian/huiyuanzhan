 #encoding=utf-8

from flask import Flask, render_template  
from flask_bootstrap import Bootstrap 
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from time import strftime, localtime
from datetime import timedelta, date
import calendar

app = Flask(__name__)

Base = declarative_base()


class Title(Base):

    __tablename__ = 'user2'
    title= Column(String(300),primary_key=True)
    name=  Column(String(300))
    time=  Column(datetime())


class User(Base):

    __tablename__ = 'user'
    user = Column(String(50),primary_key=True)
    password = Column(String(50))
    time=Column(String(20))
    

engine = create_engine('mysql+mysqldb://root:root@127.0.0.1/user?charset=utf8',echo=True)
DBSession = sessionmaker(bind=engine)
session = DBSession()

aa=session.query(Title).all()

#titlename=session.query(Title.title).limit(10).all()
titlename=session.query(Title.title).filter(Title.title.like("%爱奇艺%")).order_by(desc(time)).limit(1).all()
titlename= str(titlename).replace('u\'','\'').decode("unicode-escape")
titlename=titlename[3:]
titlename=titlename[:-10]

@app.route("/")
def index():
    year = strftime("%Y",localtime())
    mon  = strftime("%m",localtime())
    day  = strftime("%d",localtime())
    hour = strftime("%H",localtime())

    return render_template('index.html',year=titlename)
 
@app.route("/<new>")
def time():


    info_time = {'year':bb, 'month':xx}
    return render_template('index.html',year=info_time)



if __name__ == "__main__":
    app.run(
        host="127.0.0.1", 
        port=8044, 
        debug=True)