# -*- coding: utf-8 -*-
import scrapy
from TomSpider.items import TomspiderItem

class TomVideoSpider(scrapy.Spider):
    name = 'tom_video'
    allowed_domains = ['tom296.com']

    start_urls = ['https://tom296.com/yazhouqingse']

    def parse(self, response):
        item = TomspiderItem()
        for list_box in response.xpath('//div[6]/div/div[3]/div[2]/div'):
            img_wrap = list_box.xpath('./div[@class="img_wrap"]/a')
            item['img_src'] = img_wrap.xpath('./[@href]')
            item['gif_src'] = img_wrap.xpath('./[@alt]')
            yield item
        pass
