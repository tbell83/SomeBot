#!venv/bin/python
from flask import Flask, request, Response, jsonify
from flask_restful import Resource, Api, reqparse
import json
import requests
import os
import subprocess
import untangle
from xml.etree import ElementTree

slack_token = 'u35qbbrVjTk7I7mzFuPuEQC1'

app = Flask(__name__)
api = Api(app)

def getMlsUrl(mlsId):
  Url = 'http://www.realtor.com/realestateandhomes-search?mlslid={0}'.format(mlsId)
  userAgent = 'Mozilla/5.0 (X11; Linux x86_64; rv:21.0) Gecko/20100101 Firefox/21.0'
  headers = {'User-Agent': userAgent}
  r = requests.get(Url, headers=headers)
  return r.url


def getDefinition(word):
  apiKey = '52935ccf-85b9-40fa-9461-0a53fc256b4e'
  url = 'http://www.dictionaryapi.com/api/v1/references/collegiate/xml/{0}?key={1}'.format(word, apiKey)
  r = requests.get(url)
  tree = ElementTree.fromstring(r.content)
  definitions = []
  for entry in tree[0].findall('def'):
    for definition in entry.findall('dt'):
        definitions.append(definition.text)

  return definitions


class SomeBot(Resource):
  def post(self):
    try:
      responseText = request.form['token']
    except:
      return Response(status=400)

    slack_input = request.form['text']
    command = slack_input.split(' ')[0]

    if command == 'define':
      word = slack_input.split(' ')[1]
      definitions = getDefinition(word)
      response_text = '{0}:\n'.format(word)
      for definition in definitions:
          response_text = '{0}{1}\n'.format(response_text, definition)
    else:
      response_text = 'You need to ask me something.'

    resp_json = {"response_type": "in_channel","text": response_text,"attachments": [{"text": response_text}]}
    return resp_json


class GitUpdate(Resource):
  def post(self):
    try:
      subprocess.Popen(['git', 'pull', 'origin', 'master'],cwd='/home/tbell/slack.tombell.io/slack_api')
      subprocess.Popen(['touch','restart.txt'],cwd='/home/tbell/slack.tombell.io/tmp/')
      return jsonify({'msg': 'Success'})
    except subprocess.CalledProcessError as error:
      return jsonify({'msg': 'Failure'})


api.add_resource(SomeBot, '/')
api.add_resource(GitUpdate, '/git')

if __name__ == '__main__':
  app.run(debug=True)
