# eddies
# midpoint and radius from felix
# rachael's last

from makePrediction import make_prediction
from googleMaps import search_cuisineAll
from felixfunctions import get_avg_spending_v2, final_area
from firebaseClient import FirebaseClient

def get_cost(price):
  return price/10

def find_optimal_location(user_ids):
  fb = FirebaseClient()

  users = []
  for doc in fb.db.collection('users').stream():
    if doc.id in user_ids:
      users.append(doc.to_dict())

  top_categories = make_prediction(users)
  price = get_avg_spending_v2(users)

  tot_locs = []
  for doc in fb.db.collection('users').stream():
    if doc.id in user_ids:
      for t in fb.db.collection('users').document(doc.id).collection('transactions').stream():
        tot_locs.append(t.to_dict()["coordinates"])

  _, center, radius = final_area(tot_locs)

  cost = get_cost(price)

  return search_cuisineAll(cost, top_categories, center, radius)

# places = find_optimal_location(["4Y6QaMGYMreONwXVM04t", "4tFUneEDRGBBEUsxxKLR"])