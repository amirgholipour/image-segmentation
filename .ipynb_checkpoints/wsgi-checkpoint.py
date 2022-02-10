import json
from flask import Flask, jsonify, request
from prediction import predict
from numpy import  array
application = Flask(__name__)


@application.route('/')
@application.route('/status')
def status():
    return jsonify({'status': 'ok'})


@application.route('/predictions', methods=['POST'])
def object_detection():
    data = request.data or '{}'
    body = json.loads(data)
    return jsonify(predict(body).numpy().tolist())
