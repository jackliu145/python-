# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhipinspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    salary = scrapy.Field()
    compony = scrapy.Field()
    work_addr = scrapy.Field()
    seniority = scrapy.Field()
    education = scrapy.Field()
    pass
