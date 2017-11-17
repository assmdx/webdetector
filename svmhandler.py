import svm
import svmutil

class svmhandler(object):
	def __init__(self):                
		pass
	def trainmodel(self,train,cv,test,modelsavepath):
		y,x = svmutil.svm_read_problem(train)#读入训练数据
		# ycv,xcv = svm_read_problem(cv)#读入验证集
		# ytest,xtest=svm_read_problem(test)#读入测试集
		prob  = svm.svm_problem(y, x)
		param = svm.svm_parameter('-t 2 -c 0.5 -g 0.125 -b 1')		
		model = svmutil.svm_train(prob, param)				
		yt,xt = svmutil.svm_read_problem(train)#???????????
		p_labs, p_acc, p_vals = svmutil.svm_predict(yt, xt, model,'-b 1')
		svmutil.svm_save_model(modelsavepath, model)#save model
		# model = svmutil.svm_load_model('model_file')#读取model
		pass

if __name__ == '__main__':
	ss = svmhandler()
	train = 'E:\\webApp\\DATA\\webdetector\\train.txt'
	cv = ''
	test = 'E:\\webApp\\DATA\\webdetector\\test.txt'
	modelsavepath =  'E:\\webApp\\DATA\\webdetector\\model\\model.txt'
	ss.trainmodel(train,cv,test,modelsavepath)
	pass
