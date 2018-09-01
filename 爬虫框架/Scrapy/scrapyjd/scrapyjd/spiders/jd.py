# -*- coding: utf-8 -*-
import scrapy
from scrapyjd.items import ScrapyjdItem
from scrapy_splash import SplashRequest
from urllib.parse import quote

script = """
function main(splash, args)
  assert(splash:go(args.url))
  assert(splash:wait(3))
  js = "window.scrollTo(0, document.body.scrollHeight)"
  splash:evaljs(js)
  assert(splash:wait(args.wait))
  js1 = string.format("document.querySelector('.p-skip input.input-txt').value = %d;document.querySelector('span.p-skip a.btn.btn-default').click();", args.page)
  splash:evaljs(js1)
  assert(splash:wait(args.wait))
  js = "window.scrollTo(0, document.body.scrollHeight)"
  splash:evaljs(js)
  assert(splash:wait(args.wait))
  return splash:html()
end
"""

class JdSpider(scrapy.Spider):
    name = 'jd'
    allowed_domains = ['jd.com']
    start_urls = ['http://jd.com/']
    base_url = 'https://search.jd.com/Search?keyword={}&enc=utf-8'

    def start_requests(self):
        keyword = self.settings.get('KEYWORD')
        for page in range(1, self.settings.get('MAX_PAGE') + 1):
            url = self.base_url.format(quote(keyword))
            yield SplashRequest(url, callback=self.parse, endpoint='execute', args={'lua_source': script, 'page': page, "wait": 8})

    def parse(self, response):
        products = response.css('#J_goodsList ul li.gl-item')
        for product in products:
            item = ScrapyjdItem()
            item['title'] = ''.join(product.css('div.p-name a em::text').extract()).strip()
            item['price'] = '￥' + product.css('div.p-price strong i::text').extract_first()
            item['shop'] = product.css('div.p-shop a::attr(title)').extract_first()
            item['comment'] = product.css('div.p-commit strong a::text').extract_first() + '条评论'
            if product.css('div.p-img img::attr(data-lazy-img)').extract_first() == 'done':
                item['image'] = 'http:' + str(product.css('div.p-img img::attr(src)').extract_first())
            else:
                item['image'] = 'http:' + str(product.css('div.p-img img::attr(data-lazy-img)').extract_first())
            yield item
