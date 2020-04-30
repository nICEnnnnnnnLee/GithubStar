# -*- coding: utf-8 -*-
import scrapy
import json
from ..items import GithubstarerItem


class BilibiliLiveRecorderSpider(scrapy.Spider):
    name = 'BilibiliLiveRecorder'
    allowed_domains = ['api.github.com']
    start_urls = ['https://api.github.com/repos/nICEnnnnnnnLee/BilibiliLiveRecorder/stargazers']
    page = 1
    
    def parse(self, response):
        print(response.text)
        result = json.loads(response.text)
        if len(result) == 0:
           return
       
        i = self.page*30 - 30
        for i_user in result:
            starer = GithubstarerItem()
            starer['serial_number'] = i
            starer['user_name'] = i_user['login']
            i += 1 
            print(starer)
            yield starer
            
        # 解析下一页
        self.page += 1
        next_link = 'https://api.github.com/repos/nICEnnnnnnnLee/BilibiliLiveRecorder/stargazers?page=%d'%self.page
        yield scrapy.Request(next_link, callback=self.parse)

