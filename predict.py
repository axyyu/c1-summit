from __future__ import absolute_import, division, print_function
from tensorflow import keras
from Profile import *
from createNewProfile import *
import requests
import json
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import sys
from firebase_admin import credentials, firestore
import firebase_admin
import random
import math


FACTORS = 5

tot_trans = []
trans_by_user = []
cred = credentials.Certificate("./server/firebase.json")
firebase_admin.initialize_app(cred)

db = firestore.client()
temp = db.collection('users').stream()
for doc in temp:
	temp_user = []
	trans = db.collection('users').document(doc.id).collection('transactions').stream()
	for x in trans:
		tot_trans.append(x.to_dict())
		temp_user.append(x.to_dict())
	trans_by_user.append((doc.id, temp_user))


cuisines = []
time_of_day = []
time_of_year = []
price_point = []
lat_ = []
long_ = []


unique_tags = []

tot_category_sum = {}
for i in range(len(trans_by_user)):
	curr = trans_by_user[i]
	user = curr[0]
	users_t = curr[1]
	created = create_person(users_t, None)
	for key,value in created.category_scores.items():
		if key in tot_category_sum:
			tot_category_sum[key] += value
		else:
			tot_category_sum[key] = value

sorted_sums = []
for k,v in tot_category_sum.items():
	sorted_sums.append((k,v))

sorted_sums = sorted(sorted_sums, key = lambda x: x[1])
sorted_sums.reverse()
NUM_TOP = 15
top_categories = [str(cuisine[0]) for cuisine in sorted_sums[:NUM_TOP + 1]]
print(top_categories)



# # raw = firebase json data
# for transaction in tot_trans:
# 	for tag in transaction[u'category']:
# 		if tag not in top_categories:
# 			continue
# 		cuisines.append(tag)
# 		time_of_day.append(int(str(transaction[u'time'])[:2]))
# 		time_of_year.append(int(str(transaction[u'date'])[:2]))
# 		price_point.append(int(str(transaction[u'amount'])))
# 		lat_.append(float(str(transaction[u'coordinates'][0])))
# 		long_.append(float(str(transaction[u'coordinates'][1])))
# for i in range(len(cuisines)):
# 	cuisines[i] = top_categories.index(cuisines[i])


# train_data = np.zeros((len(tot_trans), FACTORS))
# train_labels = np.zeros((len(tot_trans), 1))


# for i in range(len(cuisines)):
# 	train_data[i] = np.array([time_of_day[i], time_of_year[i], price_point[i], lat_[i], long_[i]])
# 	train_labels[i] = cuisines[i]

# def build_model(train_data):
# 	model = keras.Sequential([
# 		keras.layers.Dense(64, activation=tf.nn.relu, input_shape=(train_data.shape[1],)),
# 		keras.layers.Dense(len(unique_tags), activation=tf.nn.relu),
# 		keras.layers.Dense(1)
# 	])

# 	# optimizes our model
# 	optimizer = tf.train.RMSPropOptimizer(0.001)
# 	model.compile(loss='mse', optimizer=optimizer, metrics=['mae'])
# 	return model

# def train(data):
# 	model = build_model(data[0])
# 	model.fit(data[0], data[1], epochs=10)
# 	return model

# model = train((train_data, train_labels))
# test_data = [np.array([[8, 1, 25, 38.87, -77.00]])]
# res = model.predict(test_data)

# print(res)

# print(('floor', top_categories[int(math.floor(res))]))
# print(('ceil', top_categories[int(math.ceil(res))]))


