# -*- coding: UTF-8 -*-
import ijson
import jieba
import json
import numpy as np
class Dataprocess(object):
        def __init__(self,jsonfilename):
                self.jsonfilename = jsonfilename
        def makematrix(self,str):
                pass
        def getdatafromjsonfile(self):                
                with open(self.jsonfilename) as fp:
                        objects = ijson.items(fp,"item")
                        for obj in objects:                                                    
                                for mm in self.fenci(obj['text']):
                                        print(mm)                                
                pass                                
        def writematrixtofile(self):
                with open('spec.txt', 'r') as f:  
                spec = f.readlines()  #将特征度入到list中
                x = np.zeros((1,108))

                # y = np.zeros(())
                str = '我的妹妹没有胸没有胸没有美腿'
                for mm in self.fenci(str):
                        for sj in spec
                                if()                                        
                pass
        def fenci(self,str):                                
                sel = jieba.cut(str, cut_all=True)
                #print(type(sel))
                return sel
def test():
        foo  = Dataprocess('data.json')
        Dataprocess.getdatafromjsonfile(foo)        
if __name__== "__main__":
        test()
