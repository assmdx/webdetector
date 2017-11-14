# -*- coding: utf-8 -*-
import scrapy
import html2text
import logging
from bs4 import BeautifulSoup
from getd.items import Content
# from selenium import webdriver
class SpiderdataSpider(scrapy.Spider):
    name = 'spiderdata'    
    start_urls = [                                            
                'https://www.hongxiu.com/',
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
            if('http' in url):            
                yield scrapy.Request(url, callback=self.parse)


    #@    museivaticani.va
    # name = 'spiderdata'    
    # allowed_domains = ['museivaticani.va']
    # start_urls = [
    #             'http://www.museivaticani.va/content/museivaticani/en/collezioni/musei.html'
    # ]    
    # def parse(self, response):
    #     item = Content()
    #     item['url'] = response.request.url
    #     # item['text'] = html2text.html2text(self.browser.page_source)
    #     item['text'] = html2text.html2text(response.text)        
    #     yield item        
    #     urlist = response.xpath('//article/nav/ul/li/a/@href').extract() + response.xpath('//div[@class="slide-wrapper"]/ul/li/a/@href').extract()+response.xpath('//div[@class="meta-info__infobox"]/a/@href').extract()
    #     for url in urlist:
    #         if('http' in url):
    #             pass
    #         else:
    #             url = 'http://www.museivaticani.va' + url
    #         yield scrapy.Request(url, callback=self.parse)
   

    #@https://www.metmuseum.org
    # name = 'spiderdata'    
    # allowed_domains = ['www.metmuseum.org']
    # start_urls = [
    #             # 'https://www.metmuseum.org/exhibitions/past-exhibitions',
    #             # 'https://www.metmuseum.org/exhibitions/upcoming-exhibitions'
    #             'https://www.metmuseum.org/exhibitions/current-exhibitions'
    # ]    
    # def __init__(self):
    #      self.browser = webdriver.Chrome()
    # def __del__(self):
    #     self.browser.close()
    # def parse(self, response):
    #     item = Content()
    #     item['url'] = response.request.url
    #     self.browser.get(response.request.url)        
    #     item['text'] = html2text.html2text(self.browser.page_source)        
    #     logger = logging.getLogger(__name__)
    #     logger.info(self.browser.page_source)
    #     yield item        

    #     soup = BeautifulSoup(self.browser.page_source, 'html.parser')
    #     if('current-exhibitions' in response.request.url):
    #         all_a=soup.find_all('div', class_='grid-listing__item')
    #         for a in all_a:
    #             url = 'https://www.metmuseum.org' + a.find('a')['href']
    #             yield scrapy.Request(url, callback=self.parse)
    #     elif('listings' in response.request.url):
    #         all_a=soup.find_all('li', class_='pagenav-sub__item')
    #         for a in all_a:
    #             url = 'https://www.metmuseum.org' + a.find('a')['href']
    #             yield scrapy.Request(url, callback=self.parse)
    #     elif('objects' in response.request.url):
    #         soup.find_all('figure', class_='card__standard-image')
    #         for a in all_a:
    #             url = 'https://www.metmuseum.org' + a.find('a')['href']
    #             yield scrapy.Request(url, callback=self.parse)
   
    # @http://www.britishmuseum.org
    # name = 'spiderdata'    
    # allowed_domains = ['www.britishmuseum.org']
    # start_urls = [                
    #             'http://www.britishmuseum.org/whats_on.aspx'
    # ]        
    # def parse(self, response):
    #     item = Content()
    #     item['url'] = response.request.url        
    #     item['text'] = html2text.html2text(response.text)                
    #     yield item                                        
    #     for url in response.xpath('//a/@href').extract():            
    #         if('http' in url):
    #             pass
    #         elif(url[0] == '/'):
    #             url = 'http://www.britishmuseum.org' + url
    #         else:
    #             url = 'http://www.britishmuseum.org/' + url
    #         yield scrapy.Request(url, callback=self.parse)        