# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DbLab1Item(scrapy.Item):
    title = scrapy.Field()
    author = scrapy.Field()
    stars = scrapy.Field()
