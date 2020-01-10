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
import datetime
import statistics
from firebaseClient import FirebaseClient

def machineLearning(users, tot_trans, top_categories, price):
  FACTORS = 3

  cuisines = []
  time_of_day = []
  time_of_year = []
  price_point = []
  lat_ = []
  long_ = []

  # raw = firebase json data
  for transaction in tot_trans:
    for tag in transaction[u'category']:
      if tag not in top_categories:
        continue
      cuisines.append(tag)
      time_of_day.append(int(str(transaction[u'time'])[:2]))
      time_of_year.append(int(str(transaction[u'date'])[:2]))
      price_point.append(int(str(transaction[u'amount'])))
      lat_.append(float(str(transaction[u'coordinates'][0])))
      long_.append(float(str(transaction[u'coordinates'][1])))
  for i in range(len(cuisines)):
    cuisines[i] = top_categories.index(cuisines[i])


  train_data = np.zeros((len(cuisines), FACTORS))
  train_labels = np.zeros((len(cuisines), 1))


  for i in range(len(cuisines)):
    train_data[i] = np.array([time_of_day[i], time_of_year[i], price_point[i]])
    train_labels[i] = cuisines[i]

  def build_model(train_data):
    model = keras.Sequential([
      keras.layers.Dense(len(top_categories), activation=tf.nn.relu, input_shape=(train_data.shape[1],)),
      keras.layers.Dense(128, activation=tf.nn.relu),
      keras.layers.Dense(1)
    ])

    # optimizes our model
    optimizer = tf.compat.v1.train.RMSPropOptimizer(0.001)
    model.compile(loss='mse', optimizer=optimizer, metrics=['mae'])
    return model

  def train(data):
    model = build_model(data[0])
    model.fit(data[0], data[1], epochs=10)
    return model

  model = train((train_data, train_labels))


  dt = datetime.datetime.now()
  input_hour = dt.hour
  input_month = dt.month
  input_spend = price

  res = model.predict(np.array([[input_hour, input_month, input_spend]]))
  print(('floor', top_categories[int(math.floor(res))]))
  print(('ceil', top_categories[int(math.ceil(res))]))

  recommendations = [top_categories[int(math.ceil(res))], top_categories[int(math.floor(res))]]
  return recommendations