from .firebaseClient import FirebaseClient
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