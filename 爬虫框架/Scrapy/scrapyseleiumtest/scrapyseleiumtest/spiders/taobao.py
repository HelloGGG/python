# -*- coding: utf-8 -*-
import scrapy
from urllib.parse import quote
from scrapy import Request
from scrapyseleiumtest.items import ProductItem

class TaobaoSpider(scrapy.Spider):
    name = 'taobao'
    allowed_domains = ['s.taobao.com']
    base_url = 'https://s.taobao.com/search?q='

    def start_requests(self):
        for keyword in self.settings.get('KEYWORDS'):
            for page in range(1, self.settings.get('MAX_PAGE') + 1):
                url = self.base_url + quote(keyword)
                yield Request(url=url, callback=self.parse, meta={'page': page}, dont_filter=True)


    def parse(self, response):
        products = response.css('div.grid-item.col')
        for product in products:
            item = ProductItem()
            item['price'] = product.css('.info-cont span.price.g_price.g_price-highlight strong::text').extract_first(),
            item['title'] = product.css('.info-cont .title-row a::attr(title)').extract_first()
            item['deal'] = product.css('.info-cont .col.end span.week-sale .num::text').extract_first()
            yield item


