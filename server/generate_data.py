from firebaseClient import FirebaseClient, credit_cards
from DataGeneration import YelpClient 
from createNewProfile import create_person
import random

def generate_sample_user(fb, yc, price):
  user = fb.generate_user()[1].get()
  res_list = yc.generate_venue_set()
  # print(res_list)
  print(user.id)
  fb.generate_transactions(user.id, res_list, price-10, price+10)

def generate_data():
  yc = YelpClient()
  fb = FirebaseClient()
  # fb.reset()
  price = 15

  for x in range(9):
    generate_sample_user(fb,yc, price)
    price+=5

  user_profiles()

def update_users():
  fb = FirebaseClient()
  for user in fb.db.collection('users').get():
    card = random.choice(credit_cards)
    points = random.randint(100, 8000)
    ref = fb.user_ref(user.id)
    ref.update({'card': card, 'points': points})

def user_profiles():
  fb = FirebaseClient()
  for user in fb.db.collection('users').stream():
    print(user.id)
    transactions = []
    for t in fb.user_ref(user.id).collection('transactions').stream():
      transactions.append(t.to_dict())

    person = create_person(transactions)

    ref = fb.user_ref(user.id)

    payload = {
      'favorites': person.favorites, 
      'totalSpent': person.totalSpent,
      'averageSpending': person.averageSpending,
      'medianSpending': person.medianSpending,
      'category_scores': person.category_scores
    }

    print(payload)
    ref.update(payload)


# user_profiles()