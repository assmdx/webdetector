# -*- coding: UTF-8 -*-
import ijson
import jieba
import json
import re
import io  
import codecs
import sys
import numpy as np
class Dataprocess(object):
        def __init__(self,jsonfilename):                
                self.jsonfilename = jsonfilename        
        #获取样本json文件
        def getdatafromjsonfile(self):                
                with open(self.jsonfilename) as fp:
                        objects = ijson.items(fp,"item")
                        for obj in objects:                                                    
                                for mm in self.fenci(obj['text']):
                                        yield mm
                pass
        def writematrixtofile(self):
                f = open('E:\\webApp\\DATA\\webdetector\\spec.txt','rb')
                spec = f.readlines()
                # for i in range(len(spec)):
                #         print(spec[i].decode(encoding="utf-8"))
                f.close()                
                # y = np.zeros(())                
                #从txt文件中读取负样本数据
                sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码
                # ffff = open('E:\\webApp\\DATA\\webdetector\\data3\\result.txt','ab+')
                x = np.zeros((244,108))
                for i in range(244): #对负样本进行迭代                        
                        filename = str(i).zfill(4) + ".txt"                        
                        f1 = codecs.open('E:\\webApp\\DATA\\webdetector\\data3\\' + filename  ,'rb')
                        data = f1.readlines() #将负样本中的所有的行取出来
                        for ii in range(len(data)):
                                fo = Dataprocess('data.json')
                                j = fo.clean_html(data[ii].decode('utf-8'))#每一行转码             
                                for mm in fo.fenci(j): #每一行分词,清洗
                                        for k in range(len(spec)):#遍历spec文件                                                
                                                # ffff.write(bytes("mm = ", encoding = "utf8"))
                                                # ffff.write(bytes(mm, encoding = "utf8"))                                                
                                                # ffff.write(bytes(" spec = ", encoding = "utf8"))
                                                # ffff.write(spec[k])
                                                # ffff.write(bytes(" result:", encoding = "utf8"))
                                                # ffff.write(bytes(str(mm == (spec[k].decode(encoding="utf-8").strip('\r\n'))), encoding = "utf8"))
                                                if(mm == spec[k].decode(encoding="utf-8").strip('\r\n')):
                                                        x[i,k] = 1
                        f1.close()
                np.savetxt('E:\\webApp\\DATA\\webdetector\\x.txt',x,fmt='%d',delimiter = ' ',newline='\r\n')                
        def fenci(self,str):            
                sel = jieba.cut(str, cut_all=True)                
                return sel
        def clean_html(self,str):
                str = str.replace("\t","")
                str = str.replace("\n","")
                str = str.replace("\r","")
                str = re.sub("[\s+\.\!\/_,$%^*(+\"\']+※-‘‘’’”“”| [+——！，。？?、~@#￥%……&*（）【】1234567890abcdefghijklmnopqrstuvwxyz()\\：《》]+","",str)
                return str
def test():
        foo  = Dataprocess('data.json')
        Dataprocess.writematrixtofile(foo)
if __name__== "__main__":
        test()