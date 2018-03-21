import os
import flask
from flask import jsonify

application = flask.Flask(__name__)
application.debug = True

@application.route('/sample-request')
def sample_request():
  return jsonify({"message":"Hello Devops this is production-2 version"})

@application.route('/liveness')
def liveness():
  storage = Storage()
  return "Container is Alive this is production version"

@application.route('/health')
def health():
  return "Healthy this is production version"

if __name__ == "__main__":
  application.run(host='0.0.0.0', port=3000)
