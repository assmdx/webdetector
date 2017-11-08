# -*- coding: utf-8 -*-
import scrapy
from getd.items import Content

class SpiderdataSpider(scrapy.Spider):
    name = 'spiderdata'    
    start_urls = ['http://www.cww2.net/',                
                'http://www.ribenseav.com/',
                'www.ccc36.com',                
                'https://www.google.com/search?q=%E4%B8%9C%E4%BA%AC%E7%83%AD&lr=lang_zh-CN',
                'https://www.baidu.com/s?wd=%E6%AC%A7%E7%BE%8E%E6%83%85%E8%89%B2&ie=UTF-8'
    ]
    def parse(self, response):
        item = Content()
        item['url'] = response.request.url
        str1 = ''.join(response.xpath('/html/head/title/text()').extract())
        str2 = ''.join(response.xpath('//a/text()').extract())
        str3 = ''.join(response.xpath('//p/text()').extract())
        item['text'] = str1 + str2 + str3                      
        yield item        

        for url in response.xpath('//a/@href').extract():
            yield scrapy.Request(url, callback=self.parse)
