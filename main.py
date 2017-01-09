#! /usr/bin/env python
#coding=utf-8
"""

"""

import re,datetime,time
from db import DBModel
import utils


def __title(title,title_key):
    """
    按标题过滤
    """
    if not title_key:
        return True
    for key in title_key.split('#'):
        if key in title:
            return True
    return False


def parse():
    url,title_key = utils.read_admin_config()
    more_url = ""
    #admin 配置地址
    soup = utils.get_soup(url)
    s = soup.find_all('div',id="rdgzmore")
    if s:
        for link in s:
            a = link.find('a')
            temurl = a.get('href')
            more_url =  url+temurl.split('./')[-1]    
    #更多内容链接 
    print "more_url",more_url
    soup = utils.get_soup(more_url)
    datas = {}
    mysqldb = DBModel()
    if soup:
        all = soup.find_all('li',class_="col-md-11 ")
        for li in all:
            a = li.find('a',class_="span8")
            span = li.find('span',class_="span1")
            url = a.get('href')
            title = a.get('title')
            #关键字过滤
            if not __title(title,title_key):
                continue
            date = span.get_text()[1:-1]
            text = parse_text(url)
            temp = {}
            temp["title"] = title.strip()
            temp["vardate"] = date
            #temp["url"] = url
            temp["createdate"] = str(int(time.time()))
            temp["text"] = text
            temp["image"] = 0
            temp["mid"] = utils.__md5(url)
            t = time.time()
            mysqldb.save(temp)
        mysqldb.commit()
        mysqldb.close()
            
    
def parse_text(url):
    """
    正式内容
    """
    soup = utils.get_soup(url)
    p = soup.find_all('p',align="justify")
    if not p:
        p = soup.find_all('p')
    text = ""
    for desc in p:
        str = desc.get_text()
        text += str
        text += "\n"
    return text


if __name__ == '__main__':
    parse()


