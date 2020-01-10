from flask import Flask, jsonify
from .generate_data import generate_data
from .firebaseClient import FirebaseClient

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
    # card = random.choice(credit_cards)
    #  = fb.user_ref(user.id)
    # ref.update({'card': card, 'points': points})
    pass

  return jsonify(users)

@app.route('/api/users/<id>', methods=['GET'])
def get_user_by_id(id):
  pass

@app.route('/api/location', methods=['POST'])
def get_location():
  pass
