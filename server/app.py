from flask import Flask, jsonify
from .generate_data import generate_data 

app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hello, World!'


@app.route('/data')
def data():
  generate_data()
  resp = jsonify(success=True)
  return resp


@app.route('/fav')
def fav():
  pass