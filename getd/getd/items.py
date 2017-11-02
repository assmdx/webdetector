import scrapy

#ItemLoader
class Content(scrapy.Item):
    url = scrapy.Field()
    text = scrapy.Field()     
    # stock = scrapy.Field()
    # last_updated = scrapy.Field(serializer=str)
    # 
