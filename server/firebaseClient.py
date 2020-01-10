from faker import Faker
from firebase_admin import credentials, firestore
import firebase_admin
import random

credit_cards = [
  "Quicksilver",
  "Venture",
  "VentureOne",
  "Savor",
  "QuicksilverOne"
]

def randomDateGenerator():
  extraDay = [1,0,1,0,1,0,1,1,0,1,0,1]
  month = random.randint(1,12)
  if(extraDay[month-1]==1):
    day = random.randint(1,31)
  else:
    day = random.randint(1,30)
  if month == 2:
    day = random.randint(1,28)
  year = random.randint(17,19)
  if len(str(month)) == 1:
    month = "0" + str(month)
  else:
    month = str(month)
  if len(str(day)) == 1:
    day = "0" + str(day)
  else:
    day = str(day)
  return month + "/" + day + "/" + str(year)

def randomTimeGenerator():
  hour = random.randint(12,20)
  mins = random.randint(1,59)
  sec = random.randint(1,59)
  if len(str(hour)) == 1:
    hour = "0" + str(hour)
  if len(str(mins)) == 1:
    mins = "0" + str(mins)
  if len(str(sec)) == 1:
    sec = "0" + str(sec)
  return str(hour) + ":" + str(mins) + ":" + str(sec)

class FirebaseClient():

  def __init__(self):
    try:
      cred = credentials.Certificate('./firebase.json')
      firebase_admin.initialize_app(cred)
    except Exception as err:
      print(err)

    self.db = firestore.client()
    self.faker = Faker()

  def reset(self):
    docs = self.db.collection('users').stream()

    for doc in docs:
      doc.reference.delete()

  ''' USER '''

  def user_ref(self,user_id):
    return self.db.collection('users').document(user_id)

  def generate_user(self):
    card = random.choice(credit_cards)
    points = random.randint(100, 8000)
    return self.add_user(self.faker.first_name(), self.faker.last_name(), card, points)

  def add_user(self, first, last, card, points):
    user = {
      "first":first, 
      "last":last,
      "card": card,
      "points": points,
    }
    return self.db.collection('users').add(user)

  ''' TRANSACTION '''

  def transaction_ref(self,user_id, transaction_id):
    return self.db.collection('users').document(user_id).collection('transactions')

  def generate_transactions(self,user_id, res_list, price_min, price_max, num_to_add=1000):
    for n in range(num_to_add):
      place = random.choice(res_list)
      time = randomTimeGenerator()
      date = randomDateGenerator()
      amount = random.randrange(price_min, price_max)
      self.add_transaction(user_id, place["name"], place["address"], place["coordinates"], amount, time, date, place["categories"])

  def add_transaction(self,user_id, name, location, coordinates, amount, time, date, category):
    transaction = {
      "name": name,
      "location": location,
      "coordinates": coordinates,
      "amount": amount,
      "time": time,
      "date": date,
      "category": category
    }

    return self.user_ref(user_id).collection('transactions').add(transaction)
