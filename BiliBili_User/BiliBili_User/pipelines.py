# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import MySQLdb


class BilibiliUserPipeline(object):
    def process_item(self, item, spider):
        return item

class BiliBiliUserInfoPipeline(object):
    def process_item(self, item, spider):
        conn = MySQLdb.connect('localhost', 'root', '.123456Abc', 'python')
        cur = conn.cursor()

        # name = item['name']
        # mid = item['mid']
        # sex = item['sex']
        # face = item['face']
        # level = item['level']
        # coins = item['coins']
        # fans = item['fans']
        # playNum = item['playNum']

        sql = '''
            insert into bilibili_User_Info(name, mid, sex, face, level, coins, fans, playNum) 
            VALUES ('%s', '%s', '%s', '%s', '%s', %s, %s, %s) 
            on DUPLICATE KEY UPDATE name=VALUES(name),sex=VALUES(sex),face=VALUES(face),level=VALUES(level),coins=VALUES(coins),fans=VALUES(fans),playNum=VALUES(playNum)
            '''%(item['name'], item['mid'], item['sex'], item['face'], item['level'], item['coins'], item['fans'], item['playNum'])

        cur.execute(sql)
        conn.commit()
        return item
