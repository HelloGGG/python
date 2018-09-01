# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field,Item

class ProductItem(Item):
    collection = 'products'
    price = Field()
    deal = Field()
    title = Field()
    shop = Field()
    location = Field()
