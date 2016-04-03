#!venv/bin/python
from flask import Flask, request, Response, jsonify
from flask_restful import Resource, Api, reqparse
import json
import requests
import os
import subprocess

slack_token = 'u35qbbrVjTk7I7mzFuPuEQC1'

app = Flask(__name__)
api = Api(app)

def getMlsUrl(mlsId):
    Url = 'http://www.realtor.com/realestateandhomes-search?mlslid={0}'.format(mlsId)
    userAgent = 'Mozilla/5.0 (X11; Linux x86_64; rv:21.0) Gecko/20100101 Firefox/21.0'
    headers = {'User-Agent': userAgent}
    r = requests.get(Url, headers=headers)
    return r.url


class SomeBot(Resource):
    def post(self):
		try:
			responseText = request.form['token']
		except:
			return Response(status=400)

		resp_json = {"response_type": "in_channel","text": responseText,"attachments": [{"text":"Partly cloudy today and tomorrow"}]}
		return resp_json

class GitUpdate(Resource):
	def post(self):
		try:
		    cmd_output = subprocess.check_output(
		        ['git', 'pull', 'origin', 'master'],)
		    return jsonify({'msg': str(cmd_output)})
		except subprocess.CalledProcessError as error:
		    return jsonify({'msg': str(error.output)})


api.add_resource(SomeBot, '/')
api.add_resource(GitUpdate, '/git')

if __name__ == '__main__':
    app.run(debug=True)
