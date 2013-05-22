#! /usr/bin/python
# -*- coding: utf-8 -*-

class Session():
    """a class for session"""
    
    def __init__(self, request_num, response_num):
        """request_num: request http's pos in the http list
        response_num: response http's pos in the http list"""
        
        self.request_num = request_num
        self.response_num = response_num
        self.http_list = []
        self.http_list.append(request_num)
        self.http_list.append(response_num)
