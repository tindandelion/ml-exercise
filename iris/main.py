from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/iris/v1/predict', methods=['POST'])
def predict():
  sample = request.json['sample']
  return jsonify({'response': sample[0]})
  
app.run(debug=True, host='0.0.0.0', port=8080)
