#! /usr/bin/env python
#coding=utf-8




class Parse(object):
    
    def __init__(self):
        self.base_url = ""
        self.key_word = ""
        self.urls = []   
        self.already_urls = []
        self.soup = ""
        self.db = ""
    
    def __db(self):
        self.db = ""
    
    def get_config_url(self):
        self.base_url = ""
        self.key_word = ""
    
    def get_soup(self,url):
        self.soup = ""
        
        
    def parse_keyword(self):
        """
        关键字过滤
        """
        pass
    
        
    def parse(self):
        pass
        
        
    def parse_text(self):
        """
        解析正文
        """
        pass
    