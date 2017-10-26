# -*- coding: utf-8 -*-
import json
import codecs
#以Json的形式存储
class SaveItem(object):
    def __init__(self):
        self.file = codecs.open('data.json', 'wb', encoding='utf-8')
    def process_item(self, item, spider):#此处可以清洗数据
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item
    def spider_closed(self, spider):
        self.file.close()
