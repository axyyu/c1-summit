# eddies
# midpoint and radius from felix
# rachael's last

from makePrediction import make_prediction
from googleMaps import search_cuisineAll
from felixfunctions import get_avg_spending_v2, final_area
from firebaseClient import FirebaseClient
from neuralNet import machineLearning

def get_cost(price):
  return price/10

def find_optimal_location(user_ids):
  fb = FirebaseClient()

  users = []
  for doc in fb.db.collection('users').stream():
    if doc.id in user_ids:
      users.append(doc.to_dict())

  trans = []
  for doc in fb.db.collection('users').stream():
    if doc.id in user_ids:
      for t in fb.db.collection('users').document(doc.id).collection('transactions').stream():
        trans.append(t.to_dict())

  price = get_avg_spending_v2(users)

  top_categories = make_prediction(users)
  recommendations = machineLearning(users, trans, top_categories, price)

  _, center, radius = final_area(trans)

  cost = get_cost(price)

  return search_cuisineAll(cost, recommendations, center, radius)

# places = find_optimal_location(["4Y6QaMGYMreONwXVM04t", "4tFUneEDRGBBEUsxxKLR"])
# print(places)