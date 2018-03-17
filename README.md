# webdetector
webdetector is a web app that recognizes whether the website is dangerous.

Developed using libsvm.

Wrapped into a Webapp using Flask Micro Framework.

# Install webdetector
To run it locally, first clone the directory.
	
	git clone https://github.com/assmdx/webdetector.git

Next cd into the directory.
	
	cd webdetector

Then install the dependencies using pip.
	
	sudo pip install -r requirements.txt

install livsvm.

To start the Flask Server,
	
	python app.py

# Doc of webdetector
https://assmdx.gitbooks.io/webdetector/content/

# Some problems

If you want to use webdetector on the dynamic website,you need to install 
webdriver and spider the url use spiderurldata method in the Dataprocess.py


