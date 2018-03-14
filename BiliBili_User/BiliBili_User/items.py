# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BilibiliUserItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class BiliBiliUserInfoItem(scrapy.Item):
    name = scrapy.Field()       #用户名
    mid = scrapy.Field()        #用户ID
    sex = scrapy.Field()        #性别
    face = scrapy.Field()       #头像
    level = scrapy.Field()      #等级
    coins = scrapy.Field()      #关注人数
    fans = scrapy.Field()       #粉丝人数
    playNum = scrapy.Field()    #播放量
