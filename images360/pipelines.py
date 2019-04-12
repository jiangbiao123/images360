# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.conf import settings
from scrapy import Request
from scrapy.exceptions import DropItem
from  scrapy.pipelines.images import ImagesPipeline


# class Mongo360Pipeline(object):
#     def __init__(self):
#         MONGO_DB = settings.get('MONGO_DB')
#         MONGO_URL = settings.get('MONGO_URL')
#         client = pymongo.MongoClient(MONGO_URL)
#         my_db = client[MONGO_DB]
#         self.post = my_db['xiazai360']
#
#     def process_item(self, item, spider):
#         self.post.insert(dict(item))
#         return item

    # def close_spider(self, spider):
    #     self.post.close()


class Image360Pipeline(ImagesPipeline):
    def file_path(self, request, response=None, info=None):
        url = request.url
        file_name = url.split('/')[-1]
        return file_name

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem('image Downloaded Failed')
        return item

    def get_media_requests(self, item, info):
        # for url in item['qhimg_url']:
        yield Request(item['qhimg_url'])




