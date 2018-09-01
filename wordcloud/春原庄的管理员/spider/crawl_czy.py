from spider import BiliBiliDamuSpider

DAMU_IDS = ['47984258', '47994079', '47997854', '48076142', '49043210', '50165357', '51334249', '52493285']
FILE_NAME = 'damu.txt';

spider = BiliBiliDamuSpider(DAMU_IDS, FILE_NAME)
spider.start_requests()