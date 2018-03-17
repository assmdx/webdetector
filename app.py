from flask import Flask, render_template,request
import sys
import os
sys.path.append(os.path.abspath("./model"))
from model import *
import Dataprocess
import model

app = Flask(__name__)

@app.route('/')
def hello_word():
	return render_template("index.html")

@app.route('/predict/',methods=['GET','POST','PUT'])
def predict():
	urlData = request.get_json()
	urlspec = Dataprocess(urlData["url"])	 
	response =model.predict(urlspec)
	return response
	
if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	app.run(debug=True)
	app.run(host='0.0.0.0',port=port)

	