# -*- coding: utf-8 -*-
import scrapy
from urllib.parse import quote
from scrapy import Request
from scrapy_splash import SplashRequest
from scrapysuning.items import ScrapysuningItem

script = """
function main(splash, args)
  assert(splash:go(args.url))
  assert(splash:wait(args.wait))
  js = string.format("document.querySelector('#bottomPage').value=%d;document.querySelector('.page-more.ensure').click()", args.page)
  splash:evaljs(js)
  assert(splash:wait(args.wait))
  return splash:html()
 end
"""


class SuningSpider(scrapy.Spider):
    name = 'suning'
    allowed_domains = ['search.suning.com']
    start_urls = ['http://search.suning.com/']
    base_url = 'http://search.suning.com/{}/'

    def start_requests(self):
        url = self.base_url.format(self.settings.get(quote('KEYWORD')))
        for page in range(1, self.settings.get('MAX_PAGE') + 1):
            yield SplashRequest(url=url, callback=self.parse, endpoint='execute', args={'lua_source': script, 'page': page, 'wait': 5})


    def parse(self, response):
        products = response.css('#filter-results .product.basic')
        for product in products:
            item = ScrapysuningItem()
            item['title'] = ''.join(product.css('div.title-selling-point a::text').extract()).strip()
            item['price'] = ''.join(product.css('div.price-box span.prive.price::text').extract()).strip()
            item['image'] = 'http:' + str(product.css('div.img-block img::attr(src)').extract_first())
            yield item