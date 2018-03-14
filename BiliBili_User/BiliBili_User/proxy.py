#-*- coding:utf-8 -*-

#from BiliBili_User.down_ips import crawl_ip
import MySQLdb
import requests
import json

conn = MySQLdb.connect('localhost', 'root', '.123456Abc', 'python')
cur = conn.cursor()

#从数据库中获取代理proxy_ip
def get_proxy_ip():
    sql = "select ip, port, ip_type from proxy_ip order by RAND() LIMIT 1"
    cur.execute(sql)
    for ip_info in cur.fetchall():
        ip = ip_info[0]
        port = ip_info[1]
        ip_type = ip_info[2]
    proxy_ip = "{0}://{1}:{2}".format(ip_type.lower(), ip, port)

    result = verify_ip(ip, ip_type, proxy_ip)
    if result:
        return proxy_ip
    else:
        return get_proxy_ip()


#验证代理ip是否现在可用
def verify_ip(ip, ip_type, proxy_ip):
    if ip_type.lower() == 'http':
        proxy_dict = {
            'http': proxy_ip
        }
    else:
        proxy_dict = {
            'https': proxy_ip
        }
    try:
        req = requests.get('https://www.baidu.com', proxies=proxy_dict, timeout=3)
        print req.status_code
    except Exception as e:
        print 'This ip is bad!' + ip
        delete_ip(ip)
        return False
    else:
        if req.status_code >= 200 and req.status_code < 300:
            return True
        else:
            delete_ip(ip)
            return False

#删除数据库中不可用的代理ip
def delete_ip(ip):
    sql = "delete from proxy_ip where ip = '{0}'".format(ip)
    cur.execute(sql)
    conn.commit()
    return True


# result = get_proxy_ip()
# print result