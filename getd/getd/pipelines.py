# -*- coding: utf-8 -*-
import json
import codecs
import re
#以Json的形式存储
class SaveItem(object):    
    def __init__(self):
        self.file = codecs.open('data.json', 'ab+', encoding='utf-8')
    def process_item(self, item, spider):#此处可以清洗数据
        if item['text']:
        	item['text'] = clean_html(self,item['text'])            
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item
    def spider_closed(self, spider):
        self.file.close()
def clean_html(self,str):
		str = str.replace("\t","")
		str = str.replace("\n","")
		str = str.replace("\r","")		
		str = re.sub("[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？?、~@#￥%……&*（）【】1234567890abcdefghijklmnopqrstuvwxyz()\\：《》]+","",str)
		return str