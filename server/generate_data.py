from .firebaseClient import FirebaseClient, credit_cards
from .DataGeneration import PullandSort
import random

def generate_sample_user(fb, price, res_list):
  user = fb.generate_user()[1].get()
  fb.generate_transactions(user.id, res_list, price-5, price+5)

def generate_data():
  res_list = PullandSort()

  fb = FirebaseClient()
  fb.reset()

  price = 15

  for x in range(4):
    generate_sample_user(fb, price, res_list)
    price+=3

def update_users():
  fb = FirebaseClient()
  for user in fb.db.collection('users').get():
    card = random.choice(credit_cards)
    points = random.randint(1000, 8000)
    ref = fb.user_ref(user.id)
    ref.update({'card': card, 'points': points})