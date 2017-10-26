# -*- coding: utf-8 -*-
import scrapy

from getd.items import Content

class SpiderdataSpider(scrapy.Spider):
    name = 'spiderdata'    
    start_urls = ['http://m.cww2.net/52/52640/7075382.html']

    def parse(self, response):
        item = Content()
        item['url'] = response.request.url
        item['title'] = response.xpath('/html/head/title/text()').extract()
        item['divtext'] = response.xpath('//div/text()').extract()               
        yield item