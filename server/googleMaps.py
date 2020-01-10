import requests
import json
import math
import time
import random


def search_cuisineAll(json_body, midpt, radius):
    # Search_cuisineALl returns a JSON of up to 60 restaurants based on the given parameters.
    # Sample Input:
    # post_body = {
    #     "cost": 1.3,
    #     "cuisineList": ["steak", "vegan", "chinese"]
    # }
    # midpt = 38.889237, -77.000165
    # radius = 8000
    def search_cuisine20(cuisine, placeList):
        APIKEY = "AIzaSyAiKw1PKQB59ICN0P4AODiRlLIuFcgUVYc"
        url = "https://maps.googleapis.com/maps/api/place/textsearch/json?query={cuisine}&type=restaurant&location={lat},{lng}&radius={radius}&opennow&minprice={minprice}&maxprice={maxprice}&key={APIKEY}".format(
            cuisine=cuisine, lat=lat, lng=lng, radius=radius, minprice=minprice, maxprice=maxprice, APIKEY=APIKEY)
        print(url)
        response = requests.get(url)
        res = json.loads(response.text)

        for result in res["results"]:
            placeList["places"].append({"name": result["name"],
                                        "formatted_address": result["formatted_address"],
                                        "latitude": result["geometry"]["location"]["lat"],
                                        "longitude": result["geometry"]["location"]["lng"],
                                        "price_level": result.get("price_level", 0),
                                        "rating": result["rating"],
                                        "user_ratings_total": result["user_ratings_total"],
                                        "cuisine": cuisine})
        return placeList
    lat, lng = midpt
    cost = json_body.get("cost")
    minprice, maxprice = int(math.floor(cost)), int(math.ceil(cost))
    cuisineList = json_body.get("cuisineList")
    radius = int(radius)
    placeList = {'places': []}

    for x in cuisineList:
        placeList = search_cuisine20(cuisine=x, placeList=placeList)

    return json.dumps(placeList)
