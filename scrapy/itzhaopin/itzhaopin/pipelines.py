from twisted.enterprise import adbapi
import MySQLdb
import MySQLdb.cursors
from scrapy.crawler import Settings as settings
import time
class JsonWithEncodingTencentPipeline(object):

    def __init__(self):

        dbargs = dict(
            host = '127.0.0.1' ,
            db = 'user',
            user = 'root', #replace with you user name
            passwd = 'root', # replace with you password
            charset = 'utf8',
            cursorclass = MySQLdb.cursors.DictCursor,
            use_unicode = True,
            )    
        self.dbpool = adbapi.ConnectionPool('MySQLdb',**dbargs)


    '''
    The default pipeline invoke function
    '''
    def process_item(self, item,spider):
            res = self.dbpool.runInteraction(self.insert_into_table,item)
            return item

    def insert_into_table(self,conn,item):
    	        aa=time.strftime('%Y-%m-%d',time.localtime(time.time()))
                #conn.execute('insert into user3(name) values(%s)', (item['name']))
                conn.execute('insert into user2(name,title,time) values(%s,%s,%s)', (item['name'],item['title'],aa))