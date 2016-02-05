import os.path as path
import iris.model

from flask import Flask, jsonify, request, abort
from numbers import Number

INVALID_CONTENT_TYPE = "Request Content-Type != application/json"
MISSING_SAMPLE = "No sample entry in request JSON"
BAD_SAMPLE = "Sample must be an array of 4 numbers"

SAMPLE_SIZE = 4

class InvalidRequest(Exception):
    def __init__(self, desc):
        self.description = desc


app = Flask(__name__)
app.model = iris.model.load()

@app.route('/iris/v1/predict', methods=['POST'])
def predict():
    sample = extract_sample_from_request(request)
    validate_sample_data(sample)

    labels = app.model.predict([sample])
    return jsonify({'label': int(labels[0])})

@app.errorhandler(InvalidRequest)
def invalid_request(error):
    response = jsonify({'message': error.description})
    response.status_code = 400
    return response
  

def extract_sample_from_request(request):
    if request.content_type != 'application/json':
        raise InvalidRequest(INVALID_CONTENT_TYPE)
    if not 'sample' in request.json:
        raise InvalidRequest(MISSING_SAMPLE)

    return request.json['sample']

def validate_sample_data(sample):
    if (not isinstance(sample, list)) or len(sample) != SAMPLE_SIZE or not all_numbers(sample): 
        raise InvalidRequest(BAD_SAMPLE)

def all_numbers(sample):
    non_numbers = [v for v in sample if not isinstance(v, Number)]
    return len(non_numbers) == 0
