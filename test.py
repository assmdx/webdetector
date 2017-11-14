# # -*- coding: UTF-8 -*-
# # f = open('E:\\webApp\\DATA\\webdetector\\spec.txt','rb')
# # spec = f.readlines()
# # for i in range(len(spec)):
# # 	print(spec[i].decode(encoding="utf-8"))	
# # f.close()
# #test ok
# #E:\\webApp\\DATA\\webdetector\\data3\\0000.txt
# # -*- coding: UTF-8 -*-
# import codecs
# import chardet
# import numpy as np
# import Dataprocess
# import io  
# import sys
# import re
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码
# def clean_l(str):
# 	str = re.sub("[\\r\\n\s+\.\!\/_,$%^*(+\"\']+※-‘‘’’”“”| [+——！，。？?、~@#￥%……&*（）【】1234567890abcdefghijklmnopqrstuvwxyz()\\：《》]+","",str)
# 	return str
# with codecs.open('E:\\webApp\\DATA\\webdetector\\spec.txt', 'rb') as f:
# 	data=f.readlines()
# 	for i in range(len(data)):		
# 		# foo = Dataprocess.Dataprocess('data.json')			
# 		# j = foo.clean_html(data[i].decode('utf-8'))		
# 		# for mm in foo.fenci(data[i]):
# 		# print(bytes(data[i],encoding="utf-8"))
# 		# print(clean_l(str(data[i],encoding="utf-8").strip('r\n')))
# 		print(bytes(str(data[i],encoding="utf-8").strip('\r\n'),encoding="utf-8"))		
# 		# print(type(data[i]))
# 		a = 'asd'		
# 		a.decode(encoding="utf-8")
# 		print('00000000000000000000000000')			
# f.close()
# pass
