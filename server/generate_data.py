from firebaseClient import FirebaseClient, credit_cards
from DataGeneration import YelpClient 
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

def update_users():
  fb = FirebaseClient()
  for user in fb.db.collection('users').get():
    card = random.choice(credit_cards)
    points = random.randint(100, 8000)
    ref = fb.user_ref(user.id)
    ref.update({'card': card, 'points': points})

generate_data()