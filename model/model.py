from libsvm.python.svmutil import *
from libsvm.python.svm import *
import os

def predict(data):
	model = svm_load_model(os.path.abspath("./model/model"))
	out=[1]
	p_label, p_acc, p_val =  svm_predict(out, data.tolist(), model)
	return p_label