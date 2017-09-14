# -*- coding: utf-8 -*-

# Define here the models for your scraped items
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
import scrapy

class prettygirl(scrapy.Item):
    siteURL=scrapy.Field()
    pageURL=scrapy.Field()
    detailURL=scrapy.Field()
    title=scrapy.Field()
    fileName=scrapy.Field()
    path=scrapy.Field()
