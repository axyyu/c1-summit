from faker import Faker
from firebase_admin import credentials, firestore
import firebase_admin

class FirebaseClient():

  def __init__(self):
    cred = credentials.Certificate("./firebase.json")
    firebase_admin.initialize_app(cred)

    self.db = firestore.client()
    self.faker = Faker()

  ''' USER '''

  def user_ref(user_id):
    return self.users.document(user_id)

  def generate_user():
    return add_user(self.faker.first_name(), self.faker.last_name(), self.faker.address())

  def add_user(first, last, address):
    user = {
      first:first, 
      last:last
    }
    return self.db.collection('users').add(user)

  ''' TRANSACTION '''

  def transaction_ref(user_id, transaction_id):
    return self.db.collection('users').document(user_id).collection('transactions')

  def generate_transactions(user_id, res_list, num_to_add):
    pass

  def add_transaction(user_id, name, location, amount, timestamp, category):
    transaction = {

    }
    return self.user_ref(user_id).add(transaction)
