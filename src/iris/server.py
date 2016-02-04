import os.path as path
import iris.model

from flask import Flask, jsonify, request


model = iris.model.load()
app = Flask(__name__)

@app.route('/iris/v1/predict', methods=['POST'])
def predict():
  sample = request.json['sample']
  labels = model.predict([sample])
  return jsonify({'label': int(labels[0])})


