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
                f = open('E:\\webApp\\DATA\\webdetector\\spec.txt','rb')
                spec = f.readlines()
                f.close()                                
                resultf = open('E:\\webApp\\DATA\\webdetector\\result.txt','ab+')
                with open(self.jsonfilename,encoding="utf-8") as fp:
                        counter  = 1                        
                        objects = ijson.items(fp,"item")
                        x = np.zeros((1,108))
                        cc = 0
                        for obj in objects:#？？？？？？？？？？？？？？？？？？？？？？？？？？
                                for mm in self.fenci(obj['text']):                                        
                                        for k in range(len(spec)):#遍历spec文件                                                
                                                if(mm == spec[k].decode(encoding="utf-8").strip('\r\n')):
                                                        x[cc,k] = 1                                                                                                                        
                                cc += 1                                                        
                                x = np.row_stack((x, np.zeros((1,108))))
                                counter += 1
                                if(counter >= 4151):
                                        break
                        np.savetxt('E:\\webApp\\DATA\\webdetector\\x2.txt',x,fmt='%d',delimiter = ' ',newline='\r\n')
                fp.close()
                resultf.close()                                        
        
        def writematrixtofile(self):
                f = open('E:\\webApp\\DATA\\webdetector\\spec.txt','rb')
                spec = f.readlines()
                # for i in range(len(spec)):
                #         print(spec[i].decode(encoding="utf-8"))
                f.close()                
                # y = np.zeros(())                
                #从txt文件中读取负样本数据
                sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码                
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
        def datatolibsvmdata(self,inputx,inputy,output):
                txt = open(inputx,'r')
                txty = open(inputy,'r')
                svm_data = open(output,'w')

                linex = txt.readlines()
                liney = txty.readlines()
                for j in range(len(linex)):
                        features = linex[j].split(' ')       
                        num = len(features)                        
                        svm_format = liney[j].strip('\t\n')
                        for i in range(num):
                                svm_format = "%s %d:%s" % (svm_format,i+1,features[i])
                                # print(i)
                        # svm_format = svm_format + '\n'
                        svm_data.write(svm_format)
                        # print svm_format
                txt.close()
                txty.close()
                svm_data.close()
                pass
def test():
        foo  = Dataprocess('E:\\webApp\\DATA\\webdetector\\data.json')
        inputx = 'E:\\webApp\\DATA\\webdetector\\x2.txt'
        inputy = 'E:\\webApp\\DATA\\webdetector\\y2.txt'
        output = 'E:\\webApp\\DATA\\webdetector\\libsvm_x_y2.txt'
        Dataprocess.datatolibsvmdata(foo,inputx,inputy,output)
if __name__== "__main__":
        test()