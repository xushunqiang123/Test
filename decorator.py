#-*-coding:utf-8 -*-
__author__ = 'XuShunQiang'
import time


#投入使用的函数
def index():
    print(u"已经写好的函数")


#附加的功能函数
def add(f):
    def wrapper(*args, **kwargs):
        print("time!!",time.ctime())
        return f(*args, **kwargs)
    return wrapper


@add
def index():
    print(u"已经写好的函数")


index()