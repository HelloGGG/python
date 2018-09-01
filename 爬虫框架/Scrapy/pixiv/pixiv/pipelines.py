# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class MySQLPipeline(object):
    
    def __init__(self, mysql_host, mysql_username, mysql_password, mysql_db):
        self.mysql_host = mysql_host
        self.mysql_username = mysql_username
        self.mysql_password = mysql_password
        self.mysql_db = mysql_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mysql_host = crawler.settings.get('MYSQL_HOST'),
            mysql_username = crawler.settings.get('MYSQL_USERNAME'),
            mysql_password = crawler.settings.get('MYSQL_PASSWORD'),
            mysql_db = crawler.settings.get('MYSQL_DB')
        )

    def open_spider(self, spider):
        self.db = pymysql.connect(self.mysql_host, self.mysql_username, self.mysql_password, self.mysql_db)
        self.cursor = self.db.cursor()

    def process_item(self, item, spider):
        try:
            sql = """create table if not exists `{}` 
            (
                `id` int(11) not null auto_increment,
                `title` varchar(45) not null,
                `url` varchar(255) not null,
                `user_name` varchar(45) not null,
                `doc_id` varchar(45) not null,
                `poster_uid` varchar(45) not null,
                primary key(`id`));""".format(item.table)
            self.cursor.execute(sql)
            self.db.commit()

            data = dict(item)
            keys = ', '.join(data.keys())
            values = ', '.join(['%s'] * len(data))
            sql = "insert into %s (%s) values(%s)" %(item.table, keys, values)
            self.cursor.execute(sql, tuple(data.values()))
            self.db.commit()
            return item

        except Exception as e:
            print('数据库错误，数据回滚', e.args)
            self.db.rollback()
    
    def close_spider(self, spider):
        self.db.close()

from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy import Request

class ImagePipeline(ImagesPipeline):
    def file_path(self, request, response=None, info=None):
        url = request.url
        file_name = url.split('/')[-1]
        return file_name
    
    def item_completed(self, results, item, info):
        images_path = [x['path'] for ok, x in results if ok]
        if not images_path:
            raise DropItem('Download failed')
        return item
    
    def get_media_requests(self, item, info):
        yield Request(item['url'])

