# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TomspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field(
    # 封面图片
    img_src = scrapy.Field()
    # 动态图
    gif_src = scrapy.Field()
    # 视频时长
    v_time = scrapy.Field()
    # 名称
    name = scrapy.Field()
    # 详情页面
    detail_url = scrapy.Field()
    # 播放量
    view_num = scrapy.Field()
    pass
