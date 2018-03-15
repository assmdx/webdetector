def predict(data):
	model = svm_load_model('model')
	p_label, p_acc, p_val = model.predict()
	return 'test'