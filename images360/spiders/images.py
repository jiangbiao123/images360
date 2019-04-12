# -*- coding: utf-8 -*-
import scrapy
import json
from images360.items import Images360Item
from urllib3.request import urlencode


class ImagesSpider(scrapy.Spider):
    name = 'images'
    allowed_domains = ['image.so.com']
    # start_urls = ['http://image.so.com/']

    def start_requests(self):
        base_url = 'http://image.so.com/zj?'
        data = {'listtype': 'new',
                'temp': '1'}
        ch_list = ['video', 'beauty', 'funny', 'go']  # 这个导航内容太多了少搞点
        for ch in ch_list:
            # print(ch)
            data['ch'] = ch
            # print(data)
            for page in range(0, 50):
                data['sn'] = page*30
                # print(data)
                full_url = base_url + urlencode(data)
                # print(full_url)
                yield scrapy.Request(url=full_url, callback=self.parse)

    # def get_page(self, response):
    #     result = json.loads(response.text)
    #     self.count = result.get('lastid')
    #     yield scrapy.Request(url=self.base_url, callback=self.start_requests, dont_filter=True)

    def parse(self, response):
        result = json.loads(response.text)
        for image in result.get('list'):
            # print(image)
            if image:
                item = Images360Item()
                item['group_title'] = image.get('group_title')
                item['tag'] = image.get('tag')
                item['qhimg_url'] = image.get('qhimg_url')
                # print(len(item))
                yield item
        # pass

