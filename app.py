from flask import Flask, redirect
from flask.ext.jsonpify import jsonify
import urllib

app = Flask(__name__)

@app.route('/')
def index():
	return redirect('http://github.com/rukmal/GhCalServer')

@app.route('/<name>')
def calData(name):
	print name
	return 'it works!!'

if __name__ == '__main__':
	app.run()