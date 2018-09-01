# -*- coding: utf-8 -*-
import scrapy
from urllib.parse import urlencode
from scrapy import Request
import json
from pixiv.items import PixivItem
import re

class Top500Spider(scrapy.Spider):
    name = 'top500'
    allowed_domains = ['h.bilibili.com']
    start_urls = ['https://h.bilibili.com/']


    def start_requests(self):
        data = {
            'category':'illustration',
            'type':'hot',
            'page_num':'',
            'page_size':'20'
        }
        base_url = 'https://api.vc.bilibili.com/link_draw/v2/Doc/list?'

        for i in range(0, self.settings.get('MAX_PAGE') + 1):
            data['page_num'] = str(i)
            url = base_url + urlencode(data)
            yield Request(url)

    def parse(self, response):
        data = json.loads(response.text)
        results = data.get('data').get('items')
        for result in results:
            item = PixivItem()
            item['title'] = result.get('item').get('title')
            item['url'] = result.get('item').get('pictures')[0].get('img_src')
            item['user_name'] = result.get('user').get('name')
            item['doc_id'] = result.get('item').get('doc_id')
            item['poster_uid'] = result.get('item').get('poster_uid')
            yield item
