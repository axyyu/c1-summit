from flask import Flask, jsonify, request
from generate_data import generate_data
from firebaseClient import FirebaseClient
from optimalLocation import find_optimal_location

app = Flask(__name__)
fb = FirebaseClient()

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

# API
@app.route('/api/users', methods=['GET'])
def get_users():
  users = {}
  for user in fb.db.collection('users').get():
    users[user.id] = user.to_dict()

  return jsonify(users)

@app.route('/api/users/<id>', methods=['GET'])
def get_user_by_id(id):
  ref = fb.user_ref(id)
  return jsonify(ref.get().to_dict())

@app.route('/api/location', methods=['POST'])
def get_location():
  user_ids = request.json["user_ids"]
  print(user_ids)
  return jsonify(find_optimal_location(user_ids))
