# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ZhipinspiderPipeline(object):
    def process_item(self, item, spider):
<<<<<<< HEAD
=======
        print(item)
>>>>>>> 4d818188039a4864460a0150c2024c8d283ebbe3
        return item
