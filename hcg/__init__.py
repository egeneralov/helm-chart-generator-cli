#!/usr/bin/env python3

import argparse
import json

import requests

class helmGeneratorClient:
  '''
  Client library for Helm charts generator API.
    - endpoint for API
    - host for ingress
    - version 0.0.0
    - registry/image    
    - imageTag
    - application port
  '''
  def __init__(self, endpoint, host, version, image, imageTag, port):
    # fix endpoint
    if not endpoint.startswith('http'):
      endpoint = 'http://' + endpoint
    self.endpoint = endpoint
    self.params = {
      'host': host,
      'version': version,
      'image': image,
      'imageTag': imageTag,
      'port': int(port)
    }
    # run action
    self.filename = self.generate()

  def generate(self):
    '''
    Ask API to generate chart
    '''
    response = requests.post(
      self.endpoint + '/generate/',
      data = json.dumps(self.params)
    )
    if response.ok:
      return response.content.decode()
    raise Exception('Error reply from server: {}'.format(response.content.decode()))

  def download(self):
    '''
    Download chart .tar.gz
    '''
    self.download_url = self.endpoint + '/download/' + self.filename
    response = requests.get(self.download_url)
    if response.ok:
      self.archive = response.content
      return True
    raise Exception('Error reply from server: {}'.format(response.content.decode()))


def cli():
  parser = argparse.ArgumentParser(description='cli client for Helm Chart Generator API', usage='hcg --endpoint 127.0.0.1:8080 --host app.domain.com --port 8080 --version 3.2.1 --image user/app --tag 3.2.1 --save')
  parser.add_argument("--endpoint", required=True, help="Helm Chart Generator API")
  parser.add_argument("--host", required=True, help="ingress host")
  parser.add_argument("--port", required=True, help="application port")
  parser.add_argument("--version", required=True, help="deployment version")
  parser.add_argument("--image", required=True, help="registry.com/image")
  parser.add_argument("--tag", required=True, help="image tag")
  parser.add_argument("--save", required=False, help="download chart to current directory", action='store_true')
  #~ parser.add_argument("--silient", required=False, help="silient action", action='store_true')
  args = parser.parse_args()

  #~ print(args)
  client = helmGeneratorClient(
    endpoint = args.endpoint,
    host = args.host,
    version = args.version,
    image = args.image,
    imageTag = args.tag,
    port = args.port
  )
  #~ print(client.filename)
  #~ print(len(client.archive))
  if not args.save:
    print('{}/download/{}'.format(client.endpoint, client.filename))
  else:
    client.download()
    with open(client.filename, 'wb+') as file:
      file.write(client.archive)
    print(client.filename)

if __name__ == '__main__':
  cli()

