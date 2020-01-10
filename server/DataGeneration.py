import requests
import json
from .Restaurant_Class import *


def PullandSort():
    API_KEY = 'Qk2dfUgG4lrNZSJzUEXkU2er5jIU8iBwgRs-YxhDYoMUIloWi_vUbAeZsCpYsnimsNJG5UU4RFVXtrBHkIoLHr0IFKAvyuLKd77R2deabsJnEXmuZSyNB0FmEV0XXnYx'
    CLIENT_ID = 'BfDOXS2iHEZn79gyvf6rsw'
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


PullandSort()

return restaurants
