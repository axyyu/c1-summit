# eddies
# midpoint and radius from felix
# rachael's last

from makePrediction import make_prediction
from googleMaps import search_cuisineAll
from felixfunctions import get_avg_spending_v2, final_area, point_inside_hull_v1
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

  _, center, radius, hull = final_area(trans)

  cost = get_cost(price)

  return (search_cuisineAll(cost, recommendations, center, radius), hull)

places = find_optimal_location(["4Y6QaMGYMreONwXVM04t", "4tFUneEDRGBBEUsxxKLR"])

print(len(places))

within_convex_hull = []
for shop in places[0]['places']:
  coords = [ shop["latitude"], shop["longitude"] ]
  if point_inside_hull_v1(coords, places[1]):
    within_convex_hull.append(shop)

#print(len(places[0]['places']))
#print(len(within_convex_hull))
  
#for entry in places[0]['places']:
  #print(str(entry["latitude"])+","+ str(entry['longitude']))

print("-----")

for entry in within_convex_hull:
  print(entry)
  #print(str(entry["latitude"])+","+ str(entry['longitude']))
