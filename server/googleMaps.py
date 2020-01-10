import requests
import json
import math
import time

# Returns a JSON of up to 60 restaurants based on the given parameters.
# Input:
# {
#     "lat": 38.889237,
#     "lng": -77.000165,
#     "cost": 1.3,
#     "cuisine": "thai",
#     "radius": 8000
# }


def search_cuisineAll(json_body):
    def search_cuisine20(pagetoken, placeList):
        APIKEY = "AIzaSyAiKw1PKQB59ICN0P4AODiRlLIuFcgUVYc"
        url = "https://maps.googleapis.com/maps/api/place/textsearch/json?query={cuisine}&type=restaurant&location={lat},{lng}&radius={radius}&opennow&minprice={minprice}&maxprice={maxprice}&key={APIKEY}{pagetoken}".format(
            cuisine=cuisine, lat=lat, lng=lng, radius=radius, minprice=minprice, maxprice=maxprice, APIKEY=APIKEY, pagetoken="&pagetoken="+pagetoken if pagetoken else "")
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
                                        "user_ratings_total": result["user_ratings_total"]})
        pagetoken = res.get("next_page_token", None)
        return pagetoken, placeList
    lat = json_body.get("lat")
    lng = json_body.get("lng")
    cost = json_body.get("cost")
    minprice, maxprice = int(math.floor(cost)), int(math.ceil(cost))
    cuisine = json_body.get("cuisine")
    radius = json_body.get("radius")
    pagetoken = None
    placeList = {'places': []}

    while True:
        pagetoken, placeList = search_cuisine20(
            pagetoken=pagetoken, placeList=placeList)
        time.sleep(5)
        if not pagetoken:
            break

    return json.dumps(placeList)
