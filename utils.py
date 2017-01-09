#! /usr/bin/env python
#coding=utf-8


import md5
import config
from bs4 import BeautifulSoup
import urllib2,urllib
import datetime,time
import random


def __md5(str):
    m = md5.new()
    m.update(str)
    return m.hexdigest()


def get_proxy(proxy):
    """
    代理 
    """
    opener = urllib2.build_opener(urllib2.ProxyHandler({'http':proxy}), urllib2.HTTPHandler(debuglevel=1))
    urllib2.install_opener(opener)
    
    
def get_soup(url):
    if not url:
        return 
    time.sleep(config.TIMESLEEP)
    if config.PROXY:
        proxy = PROXY_LIST[random.randint(0,len(PROXY_LIST)-1)]
        get_proxy(proxy)
    header = config.HEADERS[random.randint(0,len(config.HEADERS))-1]
    req = urllib2.Request(url = url,headers = header)
    html = urllib2.urlopen(req).read()
    if status_code(html):
        print "爬取失败地址",url
        return False
    soup = BeautifulSoup(html)
    return soup

def status_code(html):
    statusCod = html.getcode()
    if statusCod != 200:
        return True
    return False


def read_admin_config():
    """
    读取admin.txt
    """
    txt = open("admin.txt")
    for i in txt:
        url,title_key = i.strip().split(" ")
        print "输入地址为:",url,title_key
    return url,unicode(title_key,'utf-8')