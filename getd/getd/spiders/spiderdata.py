# -*- coding: utf-8 -*-
import scrapy
from getd.items import Content

class SpiderdataSpider(scrapy.Spider):
    name = 'spiderdata'    
    start_urls = ['http://www.qq.com/']

    def parse(self, response):
        item = Content()
        item['url'] = response.request.url
        str1 = ''.join(response.xpath('/html/head/title/text()').extract())
        str2 = ''.join(response.xpath('//a/text()').extract())
        str3 = ''.join(response.xpath('//p/text()').extract())
        item['text'] = str1 + str2 + str3                      
        yield item

