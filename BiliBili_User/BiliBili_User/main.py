#-*- coding:utf-8 -*-



#进行spider的debug调试
from scrapy.cmdline import execute
import os,sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(['scrapy', 'crawl', 'bilibili_user'])