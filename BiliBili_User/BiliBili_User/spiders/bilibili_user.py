# -*- coding: utf-8 -*-
import scrapy
from BiliBili_User.items import BiliBiliUserInfoItem
import json
import requests
#from BiliBili_User.user_agent import get_user_agent

class BilibiliUserSpider(scrapy.Spider):
    name = 'bilibili_user'
    allowed_domains = ['space.bilibili.com', 'api.bilibili.com']
    start_urls = ['https://space.bilibili.com/']

    start_url = 'https://space.bilibili.com/ajax/member/GetInfo'
    header = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:58.0) Gecko/20100101 Firefox/58.0',
        'Referer': 'https://space.bilibili.com/122879'
    }
    post_data = {
        'csrf': '',
        'mid': '122879'
    }

    def start_requests(self):
        return [scrapy.FormRequest(url=self.start_url, headers=self.header, formdata=self.post_data, callback=self.parse_userInfo)]


    # def parse(self, response):
    #     pass
    def parse_userInfo(self, response):
        info = json.loads(response.body)

        userInfoItem = BiliBiliUserInfoItem()
        userInfoItem['name'] = info['data']['name']
        userInfoItem['mid'] = info['data']['mid']
        if info['data']['sex'] == '':
            userInfoItem['sex'] = u'保密'
        else:
            userInfoItem['sex'] = info['data']['sex']
        userInfoItem['face'] = info['data']['face']
        userInfoItem['level'] = info['data']['level_info']['current_level']
        userInfoItem['playNum'] = info['data']['playNum']

        #user_agent = get_user_agent()
        header = {
            #'User-Agent': user_agent,  #移到middlewares中
            'Referer': 'https://space.bilibili.com/{0}/'.format(info['data']['mid'])
        }

        fansNum_url = 'https://api.bilibili.com/x/relation/stat?vmid={0}'.format(info['data']['mid'])   #获取粉丝人数的url
        fans_req = requests.get(url=fansNum_url, headers=header)  # 获取用户的粉丝人数
        fans_texts = json.loads(fans_req.text)

        userInfoItem['fans'] = fans_texts['data']['follower']

        fowllowingsNum_url = 'https://api.bilibili.com/x/relation/stat?vmid={0}'.format(info['data']['mid'])
        followings_req = requests.get(url=fowllowingsNum_url, headers=header)  # 获取用户的关注人数
        followings_texts = json.loads(followings_req.text)

        userInfoItem['coins'] = followings_texts['data']['following']

        for num in range(1, 6): #bilibili系统设置能允许外部用户访问他人的关注人数、粉丝人数5页
            fansInfo_url = 'https://api.bilibili.com/x/relation/followers?vmid={0}&pn={1}&ps=20&order=desc'.format(
                info['data']['mid'], num)  # 获取每页粉丝的url
            yield scrapy.Request(url=fansInfo_url, headers=header, callback=self.parse_relations, dont_filter=True)

            followingsInfo_url = 'https://api.bilibili.com/x/relation/followings?vmid={0}&pn={1}&ps=20&order=desc'.format(
                info['data']['mid'], num)   # 获取每页已关注人的url
            yield scrapy.Request(url=followingsInfo_url, headers=header, callback=self.parse_relations, dont_filter=True)
        yield userInfoItem



    def parse_relations(self, response):
        relations_info = json.loads(response.body)
        for info in relations_info['data']['list']:
            mid = info['mid']
            #user_agent = get_user_agent()
            header = {
                #'User-Agent': user_agent,  #移到middlewares中
                'Referer': 'https://space.bilibili.com/{0}/'.format(mid)
            }
            post_data = {
                'csrf': '',
                'mid': str(mid)
            }
            yield scrapy.FormRequest(url=self.start_url, headers=header, formdata=post_data,
                               callback=self.parse_userInfo, dont_filter=True)


