#! /usr/bin/env python
#coding=utf-8

"""

"""
import MySQLdb as mysqldb
import config

def save(datas):
    f = open("a.txt","a")
    for i in datas:
        f.write(i)
        f.write("\n")
    f.close()
    
class DBModel(object):
    def __init__(self):
        self.db =  mysqldb.connect(db=config.DBNAME,host=config.DBHOST,user=config.DBUSER,passwd=config.DBPSWD,charset="utf8")
        self.cursor = self.db.cursor()
        
    def close(self):
        self.db.close()
        
    def commit(self):
        self.db.commit()
        
    def save(self,data):
        try:
            sql = "INSERT INTO newstitle(title,vardate, createdate, mid, image) \
                VALUES ('%s', '%s', '%s', '%s', '%d')" % \
                (data['title'],data['vardate'],data['createdate'],data['mid'],data['image'])
            self.cursor.execute(sql)
            if len(data['text']) > 250:
                data['text'] = data['text'][0:249]
            sql = """INSERT INTO newstext(
                text,mid)
                VALUES ('%s', '%s')""" % (data['text'],data['mid'])
            self.cursor.execute(sql)
        except Exception,e:
            print "sql exception",e
            #self.commit()
            self.close()
        
        



def create_table():
    """
    建表
    CREATE DATABASE IF NOT EXISTS test default charset utf8 COLLATE utf8_general_ci;
    """
    db = mysqldb.connect(db=config.DBNAME,host=config.DBHOST,user=config.DBUSER,passwd=config.DBPSWD)
    cursor = db.cursor()
    cursor.execute("DROP TABLE IF EXISTS newstext")
    cursor.execute("DROP TABLE IF EXISTS newstitle")
    sql = """
         CREATE TABLE newstext (
         text  varchar(255) NOT NULL,
         mid CHAR(32) NOT NULL
         )
        """
    cursor.execute(sql)
    print sql
    sql = """
         CREATE TABLE newstitle (
         id int(5) NOT NULL auto_increment,
         title  varchar(100) NOT NULL,
         vardate  CHAR(20) NOT NULL,
         createdate CHAR(12) NOT NULL,
         mid varchar(32) NOT NULL,
         image int(1) NOT NULL,
         PRIMARY KEY  (`id`)
         )
        """
    cursor.execute(sql)
    print sql
    db.close()
        
    
    
    
if __name__ == '__main__':
    create_table()