from flask import Flask, jsonify, request, make_response, current_app
from generate_data import generate_data
from firebaseClient import FirebaseClient
from optimalLocation import find_optimal_location
from datetime import timedelta
from functools import update_wrapper
import json

app = Flask(__name__)
fb = FirebaseClient()

@app.route('/')
# @crossdomain(origin='*')
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
# @crossdomain(origin='*')
def get_users():
  users = {}
  for user in fb.db.collection('users').get():
    users[user.id] = user.to_dict()

  return jsonify(users)

@app.route('/api/users/<id>', methods=['GET'])
# @crossdomain(origin='*')
def get_user_by_id(id):
  ref = fb.user_ref(id)
  return jsonify(ref.get().to_dict())

@app.route('/api/location', methods=['POST'])
# @crossdomain(origin='*')
def get_location():
  user_ids = request.json["user_ids"]
  #print(user_ids)
  #print(jsonify(find_optimal_location(user_ids)))
  #return jsonify(find_optimal_location(user_ids))
  return jsonify(find_optimal_location(user_ids))

# def crossdomain(origin=None, methods=None, headers=None, max_age=21600,
#                 attach_to_all=True, automatic_options=True):
#     """Decorator function that allows crossdomain requests.
#       Courtesy of
#       https://blog.skyred.fi/articles/better-crossdomain-snippet-for-flask.html
#     """
#     if methods is not None:
#         methods = ', '.join(sorted(x.upper() for x in methods))
#     # use str instead of basestring if using Python 3.x
#     if headers is not None and not isinstance(headers, basestring):
#         headers = ', '.join(x.upper() for x in headers)
#     # use str instead of basestring if using Python 3.x
#     if not isinstance(origin, basestring):
#         origin = ', '.join(origin)
#     if isinstance(max_age, timedelta):
#         max_age = max_age.total_seconds()

#     def get_methods():
#         """ Determines which methods are allowed
#         """
#         if methods is not None:
#             return methods

#         options_resp = current_app.make_default_options_response()
#         return options_resp.headers['allow']

#     def decorator(f):
#         """The decorator function
#         """
#         def wrapped_function(*args, **kwargs):
#             """Caries out the actual cross domain code
#             """
#             if automatic_options and request.method == 'OPTIONS':
#                 resp = current_app.make_default_options_response()
#             else:
#                 resp = make_response(f(*args, **kwargs))
#             if not attach_to_all and request.method != 'OPTIONS':
#                 return resp

#             h = resp.headers
#             h['Access-Control-Allow-Origin'] = origin
#             h['Access-Control-Allow-Methods'] = get_methods()
#             h['Access-Control-Max-Age'] = str(max_age)
#             h['Access-Control-Allow-Credentials'] = 'true'
#             h['Access-Control-Allow-Headers'] = \
#                 "Origin, X-Requested-With, Content-Type, Accept, Authorization"
#             if headers is not None:
#                 h['Access-Control-Allow-Headers'] = headers
#             return resp

#         f.provide_automatic_options = False
#         return update_wrapper(wrapped_function, f)
#     return decorator
