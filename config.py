#! /usr/bin/env python
#coding=utf-8
"""

cookie列表 
ip代理设置:
    启用开关
    代理地址
链接请求间隔
日志输出
数据库配置

"""

DBUSER = "root"     #数据库用户名
DBPSWD = "root"          #密码
DBNAME = "test"      #数据库名称
DBHOST = "localhost" #host

#模拟浏览器请求头列表
HEADERS = [
    {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6','Referer': 'http://www.baidu.com'},
    {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36'},
    {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14','Referer': 'http://www.baidu.com'},
    {'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_1_1 like Mac OS X) AppleWebKit/602.2.14KHTML, like Gecko) Version/10.0 Mobile/14B100 Safari/602.1'},
    {'User-Agent':'MobileSafari/602.1 CFNetwork/808.1.4 Darwin/16.1.0'},
]

COOKIES = [
    
]

#批量访问间隔单位秒
TIMESLEEP = 1

#代理
PROXY = False
PROXY_LIST = []



