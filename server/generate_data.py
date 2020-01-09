from .firebaseClient import FirebaseClient
import random

def generate_sample_user():
  user = fb.generate_user()

  num = random.randint(9,10)
  

def generate_data():
  fb = FirebaseClient()

  for x in range(3):
    generate_sample_user()