import os.path as path
import iris.model

from flask import Flask, jsonify, request, abort


model = iris.model.load()
app = Flask(__name__)

@app.route('/iris/v1/predict', methods=['POST'])
def predict():
    if request.content_type != 'application/json':
        abort(400)

    sample = request.json['sample']
    labels = model.predict([sample])
    return jsonify({'label': int(labels[0])})
  
  
