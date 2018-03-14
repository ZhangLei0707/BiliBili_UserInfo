#-*- coding:utf-8 -*-

import requests
import json
import MySQLdb

# conn = MySQLdb.connect('localhost', 'root', '.123456Abc', 'python')
# cur = conn.cursor()
#
#
# sql = "delete from proxy_ip where ip='{0}'".format('60.187.241.95')
# cur.execute(sql)
# conn.commit()
#
#
# req = requests.get('https://www.baidu.com', proxies='https://61.155.164.108:3128', timeout=3)
#
# print req.status_code


# # sql = '''
# #     insert into bilibili_User_Info(name, mid, sex, face, level, coins, fans, playNum) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
# # '''
# sql = '''insert into bilibili_User_Info(name, mid) VALUES ('%s', '%s')'''
# # cur.execute(sql, (item['name'], item['mid'], item['sex'], item['face'], item['level'], item['coins'], item['fans'], item['palyNum']))
# name = 'zhangsan'

# from fake_useragent import UserAgent
# from BiliBili_User.user_agent import get_user_agent
#
# user_agent = get_user_agent()
# # ua = UserAgent()
# print user_agent


# user_id = '122879'
# referer = 'https://space.bilibili.com/' + user_id
#
#
# header = {
#     'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:58.0) Gecko/20100101 Firefox/58.0',
#     'Referer':referer
# }
#
# post_data = {
#     'csrf':'',
#     'mid':'122879'
# }
#
# req = requests.post(url='https://space.bilibili.com/ajax/member/GetInfo', headers=header, data=post_data)
# # texts = json.loads(req.text)
# # namepate = texts['data']['nameplate']
# # i = type(namepate)
# print req.status_code


# req = requests.get('https://api.bilibili.com/x/relation/followers?vmid=5986853&pn=5&ps=20&order=desc')
# texts = json.loads(req.text)
#
# print '123'