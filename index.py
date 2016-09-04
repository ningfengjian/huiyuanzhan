 #encoding=utf-8

from flask import Flask, render_template  
from flask_bootstrap import Bootstrap 
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from flask import Markup 
from time import strftime, localtime
from datetime import timedelta, date
import calendar

app = Flask(__name__)

Base = declarative_base()


class Title(Base):

    __tablename__ = 'user2'
    title= Column(String(300),primary_key=True)
    name=  Column(String(300))
    time=  Column(String(300))


class User(Base):

    __tablename__ = 'user'
    user = Column(String(50),primary_key=True)
    password = Column(String(50))
    time=Column(String(20))
    

#engine = create_engine('mysql+mysqldb://root:root@127.0.0.1/user?charset=utf8',echo=True)
#DBSession = sessionmaker(bind=engine)

#session=session.query(Title).all()

#titlename=session.query(Title.title).limit(10).all()
#titlename=session.query(Title.title).filter(Title.title.like("%爱奇艺%")).order_by((Title.time).desc()).limit(10).all()

#titlename= str(titlename).replace('u\'','\'').replace('-\\u4e50\\u4eab\\u7f51','').replace('[(\'','').replace('\',)]','').decode("unicode-escape")

#titlename=titlename[3:]
#titlename=titlename[:-10].split("',), ('")
#print titlename
#print type(titlename)
#titlename=titlename.split("',), ('")
#session.close()
@app.route("/")
def index():
    year = strftime("%Y",localtime())
    mon  = strftime("%m",localtime())
    day  = strftime("%d",localtime())
    hour = strftime("%H",localtime())
    engine = create_engine('mysql+mysqldb://root:root@127.0.0.1/user?charset=utf8',echo=True)
    DBSession = sessionmaker(bind=engine)
    session= DBSession()
    titlename=session.query(Title.title).filter(Title.title.like("%爱奇艺%")).order_by((Title.time).desc()).limit(10).all()

    titlename= str(titlename).replace('u\'','\'').replace('-\\u4e50\\u4eab\\u7f51','').replace('[(\'','').replace('\',)]','').decode("unicode-escape")

    #titlename=titlename[3:]
    #titlename=titlename[:-10].split("',), ('")
    #print titlename
    #print type(titlename)
    titlename=titlename.split("',), ('")
    session.close()

    return render_template('index.html',titles=titlename)
 
@app.route("/aiqiyi/<new>")
def time(new):
    engine = create_engine('mysql+mysqldb://root:root@127.0.0.1/user?charset=utf8',echo=True)
    DBSession = sessionmaker(bind=engine)
    session= DBSession()
    titlename2=session.query(Title.title).filter(Title.title.like("%爱奇艺%")).order_by((Title.time).desc()).limit(20).all()

    titlename2= str(titlename2).replace('u\'','\'').replace('-\\u4e50\\u4eab\\u7f51','').replace('[(\'','').replace('\',)]','').decode("unicode-escape")
    titlename2=titlename2.split("',), ('")

    titlename=session.query(Title.name).filter(Title.title.like("%"+new+"%")).order_by((Title.time).desc()).limit(1).all()
    print titlename
    titlename= str(titlename).replace('u\'','\'').replace('\\u8d26\\u53f7','<br>\\u8d26\\u53f7').replace('[(\'','').replace('\',)]','').decode("unicode-escape")
    #info_time = {'year':bb, 'month':xx}r
    session.close()
    return render_template('shipin.html',year=titlename,new=new,titlename2=titlename2)



if __name__ == "__main__":
    app.run(
        host="127.0.0.1", 
        port=8044, 
        debug=True)