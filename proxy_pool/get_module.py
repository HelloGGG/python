import json
from pyquery import PyQuery as pq
from save_module import RedisCilent
from myutil import get_page



# 创建元类，继承元类的都具有方法名为crawl开头的方法
class ProxyMetaclass(type):
    def __new__(cls, name, bases, attrs):
        count = 0
        attrs['__CrawlFunc__'] = []
        for k,v in attrs.items():
            # 添加以crawl开头的方法
            if 'crawl_' in k:
                attrs['__CrawlFunc__'].append(k)
                count += 1
        attrs['__CrawlFuncCount__'] = count
        return type.__new__(cls, name, bases, attrs)

class Crawler(object, metaclass=ProxyMetaclass):
    # 从某个网站获得代理
    def get_proxies(self, callback):
        proxies = []
        for proxy in eval('self.{}()'.format(callback)):
            print('成功获取到代理', proxy)
            proxies.append(proxy)

        return proxies

    #选取网站爬代理
    def crawl_daili66(self, page_count=20):

        start_url = 'http://www.66ip.cn/{}/html'
        urls = [start_url.format(page) for page in range(1, page_count + 1)]
        for url in urls:
            print('Crawling', url)
            html = get_page(url)
            if html:
                doc = pq(html)
                trs = doc('.containerbox table tr:gt(0)').items()
                for tr in trs:
                    ip = tr.find('td:nth-child(1)').text()
                    port = tr.find('td:nth-child(2)').text()
                    yield ':'.join([ip, port])

    def crawl_kuaidaili(self, page_count=20):
        start_url = 'https://www.kuaidaili.com/free/inha/{}/'
        urls = [start_url.format(page) for page in range(1, page_count+1)]
        for url in urls:
            print('Crawling', url)
            html = get_page(url)
            if html:
                doc = pq(html)
                trs = doc('#list tbody tr').items()
                for tr in trs:
                    ip = tr.find('td:nth-child(1)').text()
                    port = tr.find('td:nth-child(2)').text()
                    yield ':'.join([ip, port])
                    
    # def crawl_xicidaili(self, page_count=10):

    #     start_url = 'http://www.xicidaili.com/nn/{}'
    #     urls = [start_url.format(page) for page in range(1, page_count + 1)]
    #     for url in urls:
    #          print('Crawling', url)
    #          html = get_page(url)
    #          if html:
    #             doc = pq(html)
    #             trs = doc('#ip_list tr:gt(0)').items()
    #             for tr in trs:
    #                 ip = tr.find('td:nth-child(2)').text()
    #                 port = tr.find('td:nth-child(3)').text()
    #                 yield ':'.join([ip, port])


POOL_UPPER_THERSHOLD = 10000

# 执行获取代理类
class Getter(object):

    def __init__(self):
        self.redis = RedisCilent()
        self.crawler = Crawler()
    
    def is_over_threshold(self):
        if self.redis.count() >= POOL_UPPER_THERSHOLD:
            return True
        else:
            return False

    def run(self):
        print('获取器开始执行')
        if not self.is_over_threshold():
            for callback_label in range(self.crawler.__CrawlFuncCount__):
                callback = self.crawler.__CrawlFunc__[callback_label]
                proxies = self.crawler.get_proxies(callback)
                for proxy in proxies:
                    self.redis.add(proxy)
    
