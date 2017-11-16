import svm
import svmutil
y, x = [1,-1], [{1:1, 2:1}, {1:-1,2:-1}]
prob  = svm.svm_problem(y, x)
param = svm.svm_parameter('-t 0 -c 4 -b 1')
model = svmutil.svm_train(prob, param)
yt = [1]
xt = [{1:1, 2:1}]
p_label, p_acc, p_val = svmutil.svm_predict(yt, xt, model)
print(p_label)

class svmhandler(object):
	def __init__(self):                
		pass
	def trainmodel(self,t_x,t_y,c_x,c_y,t_x,t_y,modelsavepath):
		
		pass
	# def loadmodel(modelsavepath):
	# 	pass