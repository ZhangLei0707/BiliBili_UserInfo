# -*- coding:utf-8 -*-

import requests
from BiliBili_User.user_agent import get_user_agent
from scrapy.selector import Selector
import MySQLdb

user_agent = get_user_agent()
header = {
    'User-Agent': user_agent
}

conn = MySQLdb.connect('localhost', 'root', '.123456Abc', 'python')
cur = conn.cursor()
#
#   爬取西刺免费代理网站的 代理ip并存到proxy_ip表中
#   西刺的代理IP有点不好用，可同理爬取其他代理网站
def crawl_ip():
    req = requests.get(url='http://www.xicidaili.com/nn/', headers=header)
    sel = Selector(text=req.text)
    trs = sel.css('#ip_list tr')
    for tr in trs[1:]:
        texts = tr.css('td::text').extract()
        ip = texts[0]
        port = texts[1]
        ip_type = texts[5]
        cur.execute("insert into proxy_ip(ip, port, ip_type) VALUES('{0}', '{1}', '{2}')".format(ip, port, ip_type))
        conn.commit()

#crawl_ip()
