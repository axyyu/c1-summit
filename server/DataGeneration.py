import requests
import json
from Restaurant_Class import *
from yelpapi import YelpAPI
import random

API_KEY = 'Qk2dfUgG4lrNZSJzUEXkU2er5jIU8iBwgRs-YxhDYoMUIloWi_vUbAeZsCpYsnimsNJG5UU4RFVXtrBHkIoLHr0IFKAvyuLKd77R2deabsJnEXmuZSyNB0FmEV0XXnYx'
CLIENT_ID = 'BfDOXS2iHEZn79gyvf6rsw'

DC = {
    "lat": 38.907469,
    "long": -77.0366787
}

loc_dev = 0.02
pref_size = 6

prefs = [
    "vegetarian",
    "vegan",
    "thai",
    "korean",
    "chinese",
    "steak",
    "salad",
    "italian",
    "hotpot",
    "latin"
]

class YelpClient():

    def __init__(self):
        self.yelp = YelpAPI(API_KEY)

    def get_tag_set(self):
        return random.sample(prefs, pref_size)

    def get_random_location(self):
        lat = DC["lat"] + random.uniform(-loc_dev*2, loc_dev*2)
        long = DC["long"] + random.uniform(-loc_dev*2, loc_dev*2)

        return (lat, long)

    def get_venues(self, lat, long, categories):
        venues = self.yelp.search_query(location='DC', latitude=lat, longitude=long, categories=categories, limit=50, open_now=True)
        return venues

    def generate_venue_set(self):
        lat, long = self.get_random_location()
        tags = self.get_tag_set()
        categories = ','.join(tags)
        # print(categories)
        venue_set = self.get_venues(lat, long, categories)["businesses"]
        # print(venue_set)

        venues = []
        for v in venue_set:
            categories = [c['alias'] for c in v["categories"]]

            address = str(v["location"]["address1"]) + " " + str(v["location"]["city"]) + ", " + \
                str(v["location"]["state"]) + " " + \
                str(v["location"]["zip_code"])

            venue = {
                "yelp_id": v["id"],
                "name": v["name"],
                "coordinates": [v["coordinates"]["latitude"], v["coordinates"]["longitude"]],
                "address": address,
                "categories": categories,
                "image": v["image_url"]
            }
            venues.append(venue)

        return venues
    

def PullandSort():
    loc = 'https://api.yelp.com/v3/businesses/search'
    headers = {'Authorization': 'Bearer ' + API_KEY}

    restaurants = []
    offset = 0
    check = 0
    for y in range(360//50):
        params = {'location': 'DC', 'sort_by': 'rating', 'open_now': True,
                  'categories': 'food', 'limit': '50', 'offset': str(offset)}
        raw = requests.get(loc, params=params, headers=headers)
        raw = raw.json()
        if raw["total"] == 0:
            break
        for resta in raw["businesses"]:
            print(resta)
            print("\n")
            fulladdress = str(resta["location"]["address1"]) + " " + str(resta["location"]["city"]) + ", " + \
                str(resta["location"]["state"]) + " " + \
                str(resta["location"]["zip_code"])

            categories = [c['alias'] for c in resta["categories"]]
            coordinates = [resta["coordinates"]["latitude"],
                           resta["coordinates"]["longitude"]]
            restaurants.append(Restaurant(
                resta["name"], coordinates, categories, fulladdress, resta["image_url"]))
            check += 1
        offset += 50

# yc = YelpClient()
# lat, long = yc.get_random_location()
# tags = yc.get_tag_set()
# categories = ','.join(tags)
# venue = yc.get_venues(lat, long, categories)
# print(venue)