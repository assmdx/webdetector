import scrapy

#ItemLoader
class Content(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    divtext = scrapy.Field()       
    # stock = scrapy.Field()
    # last_updated = scrapy.Field(serializer=str)
    # 
