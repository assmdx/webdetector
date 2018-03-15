# -*- coding: UTF-8 -*-
import ijson
import jieba
import json
import re
import io  
import codecs
import sys
import numpy as np

from bs4 import BeautifulSoup
from selenium import webdriver

def Dataprocess(url):
        def spiderurldata(url):
                browser = webdriver.Chrome()
                browser.get('http://php.net/') 
                soup = BeautifulSoup(browser.page_source,"html5lib")
                text = soup.get_text(strip=True)
                # print(text.encode('utf-8'))
                browser.close()
                return text.encode('utf-8')

        def getsvmdata(htmlcode):
                f = open('spec.txt','rb')
                spec = f.readlines()                
                f.close()                
                # y = np.zeros(())                
                #从txt文件中读取负样本数据
                x = np.zeros((1,108))
                j = fo.clean_html(htmlcode.decode('utf-8'))                                                                                                      
                for mm in fo.fenci(j): #每一行分词,清洗
                        for k in range(len(spec)):#遍历spec文件                                                                                                
                                if(mm == spec[k].decode(encoding="utf-8").strip('\r\n')):
                                        x[0,k] = 1
                return x                
        def fenci(str):            
                sel = jieba.cut(str, cut_all=True)                
                return sel
        def clean_html(str):
                str = str.replace("\t","")
                str = str.replace("\n","")
                str = str.replace("\r","")
                str = re.sub("[\s+\.\!\/_,$%^*(+\"\']+※-‘‘’’”“”| [+——！，。？?、~@#￥%……&*（）【】1234567890abcdefghijklmnopqrstuvwxyz()\\：《》]+","",str)
                return str
        html = spiderurldata(url)
        text = getsvmdata(html)
        return text
