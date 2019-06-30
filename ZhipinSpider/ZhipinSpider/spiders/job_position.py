# -*- coding: utf-8 -*-
import scrapy
from ZhipinSpider.items import ZhipinspiderItem

class JobPositionSpider(scrapy.Spider):
    name = 'job_position'
    allowed_domains = ['zhipin.com']
    start_urls = ['https://www.zhipin.com/c101280100/h_101280100']

    def parse(self, response):
        for job_primary in response.xpath(r'//div[@id="main"]/div/div[2]/ul/li/div'):
            item = ZhipinspiderItem()
            info_primary = job_primary.xpath('./div[@class="info-primary"]')
            item['title'] = info_primary.xpath('./h3/a/div[@class="job-title"]/text()')
            yield item