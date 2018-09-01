# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest

script = """
  assert(splash:go(args.url))
  assert(splash:wait(3))
  js = "document.getElementById('g_iframe').contentWindow.document.querySelector('.zbtn.znxt').click();"
  splash:evaljs(js)
  return splash:html()
"""

class WycommentSpider(scrapy.Spider):
    name = 'wycomment'
    allowed_domains = ['music.163.com']
    start_urls = ['http://music.163.com/']
    
    
    def start_requests(self):
        url = 'https://music.163.com/#/song?id=513791211'
        yield SplashRequest(url=url, endpoint='execute', args={'lua_source': script})

    def parse(self, response):
        pass
