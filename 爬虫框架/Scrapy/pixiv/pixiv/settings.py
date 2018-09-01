# -*- coding: utf-8 -*-

# Scrapy settings for pixiv project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'pixiv'

SPIDER_MODULES = ['pixiv.spiders']
NEWSPIDER_MODULE = 'pixiv.spiders'
MAX_PAGE = 24

MYSQL_HOST = 'localhost' 
MYSQL_USERNAME = 'root'
MYSQL_PASSWORD = '123456'
MYSQL_DB = 'spider'

IMAGES_STORE = './images'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'pixiv (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'accept-language': 'zh-CN,zh;q=0.9',
  'Referer': 'https://h.bilibili.com/eden/draw_area',
  'Origin': 'https://h.bilibili.com',
  'Cookie': 'l=v; finger=6759d89f; LIVE_BUVID=AUTO8015328699760841; fts=1532869981; sid=hycot42q; buvid3=1B09A866-4194-41E8-BD4B-84C457AFE37E94839infoc; rpdid=kmpqolqimkdoskiqmwxpw; CURRENT_FNVAL=2; stardustvideo=0; CURRENT_QUALITY=32; UM_distinctid=1653ca21ba729-062c8a221724e9-3c720356-100200-1653ca21baa15f; DedeUserID=15013871; DedeUserID__ckMd5=a6e48a729d8c1b7b; SESSDATA=1f107f8f%2C1537437418%2C96922b40; bili_jct=66daa79dff451fbe2b763e5b3fc2a4fa; im_notify_type_15013871=0; _dfcaptcha=b3975275574eb680e60baf0f9faec640',
  'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'pixiv.middlewares.PixivSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'pixiv.middlewares.PixivDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'pixiv.pipelines.ImagePipeline': 300,
   'pixiv.pipelines.MySQLPipeline': 301,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
