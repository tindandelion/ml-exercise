from flask import Flask

print __name__

app = Flask(__name__)

@app.route('/')
def index():
  return "Hello world!"

app.run(debug = True)
