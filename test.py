#检测特征文件的读取
# # # -*- coding: UTF-8 -*-
# # # f = open('E:\\webApp\\DATA\\webdetector\\spec.txt','rb')
# # # spec = f.readlines()
# # # for i in range(len(spec)):
# # # 	print(spec[i].decode(encoding="utf-8"))	
# # # f.close()
# # #test ok
# # #E:\\webApp\\DATA\\webdetector\\data3\\0000.txt

#处理爬取的数据生成矩阵
# # # -*- coding: UTF-8 -*-
# # import codecs
# # import chardet
# # import numpy as np
# # import Dataprocess
# # import io  
# # import sys
# # import re
# # sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码
# # def clean_l(str):
# # 	str = re.sub("[\\r\\n\s+\.\!\/_,$%^*(+\"\']+※-‘‘’’”“”| [+——！，。？?、~@#￥%……&*（）【】1234567890abcdefghijklmnopqrstuvwxyz()\\：《》]+","",str)
# # 	return str
# # with codecs.open('E:\\webApp\\DATA\\webdetector\\spec.txt', 'rb') as f:
# # 	data=f.readlines()
# # 	for i in range(len(data)):		
# # 		# foo = Dataprocess.Dataprocess('data.json')			
# # 		# j = foo.clean_html(data[i].decode('utf-8'))		
# # 		# for mm in foo.fenci(data[i]):
# # 		# print(bytes(data[i],encoding="utf-8"))
# # 		# print(clean_l(str(data[i],encoding="utf-8").strip('r\n')))
# # 		print(bytes(str(data[i],encoding="utf-8").strip('\r\n'),encoding="utf-8"))		
# # 		# print(type(data[i]))
# # 		a = 'asd'		
# # 		a.decode(encoding="utf-8")
# # 		print('00000000000000000000000000')			
# # f.close()
# # pass
# # 

#提取网址列表，为后面加标签做准备
# # import ijson
# # import codecs
# # fp = open('E:\\webApp\\DATA\\webdetector\\data.json',encoding="utf-8")
# # f3 = open('E:\\webApp\\DATA\\webdetector\\urlist.txt','ab+')
# # objects = ijson.items(fp,"item")
# # for obj in objects:	
# # 	f3.write(bytes(obj['url']+"\r\n",encoding="utf-8"))
# # fp.close()
# # f3.close()


# # import ijson
# # import codecs
# # # fp = open('E:\\webApp\\DATA\\webdetector\\d.json',encoding="utf-8")
# # f1 = codecs.open('E:\\webApp\\DATA\\webdetector\\data.json','rb')
# # f2 = open('E:\\webApp\\DATA\\webdetector\\data2.json','ab+')
# # f3 = open('E:\\webApp\\DATA\\webdetector\\urlist.txt','ab+')
# # data = f1.readlines() #将负样本中的所有的行取出来
# # for i in range(len(data)):
# # 	str = data[i].decode(encoding="utf-8").strip("\r\n")
# # 	f2.write(bytes(str+",\r\n",encoding="utf-8"))	
# # f2.close()
# # f1.close()
# # 
# #

# 将txt数据转化为libsvm标准格式数据
# #coding=utf-8
# # from sys import argv
# # script, input, output = argv
# input = 'E:\\webApp\\DATA\\webdetector\\x.txt'
# input2 = 'E:\\webApp\\DATA\\webdetector\\y.txt'
# output = 'E:\\webApp\\DATA\\webdetector\\libsvm_x_y.txt'
# txt = open(input,'r')
# txty = open(input2,'r')
# svm_data = open(output,'w')

# linex = txt.readlines()
# liney = txty.readlines()

# for j in range(len(linex)):
#     features = linex[j].split(' ')       
#     num = len(features)

#     svm_format = liney[j].strip('\t\n')
#     for i in range(num):
#         svm_format = "%s %d:%s" % (svm_format,i+1,features[i])
#         # print(i)
#     svm_format = svm_format + '\n'
#     svm_data.write(svm_format)
#     # print svm_format
# txt.close()
# txty.close()
# svm_data.close()
# 

#给正样本数据打标签
# import threading
# from selenium import webdriver
# browser = webdriver.Chrome()

# urlist = open('E:\\webApp\\DATA\\webdetector\\urlist.txt','r')
# linex = urlist.readlines()
# for j in range(len(linex)):
# 	url = linex[j]
# 	if(j > 2058):
# 		browser.get(url)
# browser.close()
# urlist.close()
# pass

