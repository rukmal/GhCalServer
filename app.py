from flask import Flask, redirect
from flask.ext.jsonpify import jsonify
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
	return redirect('http://github.com/rukmal/GhCalServer')

@app.route('/<username>')
def calData(username):
	requestURL = 'http://github.com/users/' + username + '/contributions_calendar_data'
	data = requests.get(requestURL)
	print (len(data.text))
	cutoff = 10000
	response = dict()
	if len(data.text) > cutoff:
		response['status'] = 'failed'
	else:
		jsonifiedData = json.loads(data.text)
		response['status'] = 'success'
		response['data'] = jsonifiedData
	return jsonify(response)

if __name__ == '__main__':
	app.run()