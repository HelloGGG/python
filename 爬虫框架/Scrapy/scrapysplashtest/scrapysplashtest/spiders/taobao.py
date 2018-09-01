# -*- coding: utf-8 -*-
import scrapy
from scrapy import Spider
from urllib.parse import quote
from scrapysplashtest.items import ProductItem
from scrapy_splash import SplashRequest




script = """
function main(splash, args)
  splash.images_enabled = false
  assert(splash:go(args.url))
  assert(splash:wait(args.wait))
  js = string.format("document.querySelector('#mainsrp-pager div.form > input').value=%d;document.querySelector('#mainsrp-pager div.form > span.btn.J_Submit').click()", args.page)
  splash:evaljs(js)
  assert(splash:wait(args.wait))
  return splash:html()
end
"""

class TaobaoSpider(scrapy.Spider):
    name = 'taobao'
    allowed_domains = ['taobao.com']
   
    base_url = 'https://s.taobao.com/search?q='

    def start_requests(self):
        for keyword in self.settings.get('KEYWORDS'):
            for page in range(1, self.settings.get('MAX_PAGE') + 1):
                url = self.base_url + quote(keyword)
                yield SplashRequest(url, callback=self.parse, endpoint='execute', args={'lua_source': script, 'page': page, 'wait': 7})

    def parse(self, response):
        products = response.css('#mainsrp-itemlist div.grid.g-clearfix div.items:nth-child(1) .item.J_MouserOnverReq')
        for product in products:
            item = ProductItem()
            item['title'] = ''.join(product.xpath('.//div[contains(@class, "title")]//text()').extract()).strip()
            item['location'] = product.css('div.location::text').extract_first()
            item['price'] = '¥' + str(product.css('.ctx-box.J_MouseEneterLeave.J_IconMoreNew div.price.g_price.g_price-highlight strong::text').extract_first())
            item['deal'] = product.css('div.ctx-box.J_MouseEneterLeave.J_IconMoreNew div.deal-cnt::text').extract_first()
            item['shop'] = product.css('a.shopname.J_MouseEneterLeave.J_ShopInfo > span:nth-child(2)::text').extract_first()
            yield item
       