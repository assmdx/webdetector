import scrapy

#ItemLoader
class Content(scrapy.Item):
    url = scrapy.Field()
    text = scrapy.Field()        
    # 
    #    