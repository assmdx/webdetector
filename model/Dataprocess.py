# -*- coding: UTF-8 -*-
import jieba
import re
import io  
import sys
import os
import numpy as np
from bs4 import BeautifulSoup
# from selenium import webdriver
import urllib

def Dataprocess(url):
        #deal with the url and get the svm input data of the url
        def urldeal(url):
                #deal with the received url
                if(url.find('http://') >= 0):
                        return url
                if(url.find('https://') >= 0):
                        return url
                else:
                        return "http://" + url

        def spiderurldata(url):
                #spider the source code of the url
                browser = webdriver.Chrome()
                browser.get(url) 
                soup = BeautifulSoup(browser.page_source,"html5lib")
                text = soup.get_text(strip=True)
                # print(text.encode('utf-8'))
                browser.close()
                return text.encode('utf-8')
        def spiderurldata2(url):
                #spider the source code of the url
                content = urllib.request.urlopen(url).read()
                soup = BeautifulSoup(content,"html5lib")
                text = soup.get_text(strip=True)
                return text.encode('utf-8')       

        def getsvmdata(htmlcode):
                # change the htmlcode to libsvm input data format
                f = open(os.path.abspath("./model/spec.txt"),'rb')
                spec = f.readlines()                
                f.close()                
                # y = np.zeros(())                
                #从txt文件中读取负样本数据
                x = np.zeros((1,108))
                j = clean_html(htmlcode.decode('utf-8'))                                                                                                      
                for mm in fenci(j): #每一行分词,清洗
                        for k in range(len(spec)):#遍历spec文件                                                                                                
                                if(mm == spec[k].decode(encoding="utf-8").strip('\r\n')):
                                        x[0,k] = 1
                return x                
        def fenci(str):
                #change the htmlcontent to word list            
                sel = jieba.cut(str, cut_all=True)                
                return sel
        def clean_html(str):
                #clean the html
                str = str.replace("\t","")
                str = str.replace("\n","")
                str = str.replace("\r","")
                str = re.sub("[\s+\.\!\/_,$%^*(+\"\']+※-‘‘’’”“”| [+——！，。？?、~@#￥%……&*（）【】1234567890abcdefghijklmnopqrstuvwxyz()\\：《》]+","",str)
                return str
        url = urldeal(url)
        html = spiderurldata2(url)
        text = getsvmdata(html)
        return text
