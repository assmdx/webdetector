from libsvm.python.svmutil import *
from libsvm.python.svm import *
import os

def predict(data):
	#predict the result of the url
	model = svm_load_model(os.path.abspath("./model/model"))
	out=[1]
	p_label, p_acc, p_val =  svm_predict(out, data.tolist(), model)
	if p_label[0] > 0.0:
		return "a dangerous website"
	else:
		return "a good website"