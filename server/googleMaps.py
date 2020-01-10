import requests
import json
import math

def search_cuisine20(pagetoken, placeList):
        APIKEY = "AIzaSyAiKw1PKQB59ICN0P4AODiRlLIuFcgUVYc"
        post_body = json.loads(request.data)
        # {
        #     "lat": 38.889237,
        #     "lng": -77.000165,
        #     "cost": 0.3,
        #     "cuisine": "thai"
        # }
        lat = post_body.get("lat")
        lng = post_body.get("lng")
        cost = post_body.get("cost")
        minprice, maxprice = math.floor(cost), math.ceil(cost)
        cuisine = post_body.get("cuisine")
        radius = 8000

        url = "https://maps.googleapis.com/maps/api/place/textsearch/json?query={cuisine}&type=restaurant&location={lat},{lng}&radius={radius}&opennow&minprice={minprice}&maxprice={maxprice}&fields=formatted_address,name,opening_hours,rating&key={APIKEY}{pagetoken}".format(
            cuisine=cuisine, lat=lat, lng=lng, radius=radius, minprice=minprice, maxprice=maxprice, APIKEY=APIKEY, pagetoken="&pagetoken="+pagetoken if pagetoken else "")
        # print(url)
        response = requests.get(url)
        res = json.loads(response.text)
        # print(res)
        # print("here results ---->>> ", len(res["results"]))

        for result in res["results"]:
            info = ";".join(map(str, ["\n", result["name"], result["formatted_address"],
                                      result.get("price_level",
                                                 0), result["rating"],
                                      result["user_ratings_total"]]))
            placeList = placeList + info
            print(info)
        pagetoken = res.get("next_page_token", None)
        print("here -->> ", pagetoken)
        return pagetoken, placeList

    ## pagetoken = "CpQFhwIAADQWOcVI1wll-B869Z24El48rXw18gKoab_keD65V18zFEvPjKIfrS79Pc_vXJcZQtOuF0RObQG20ph-GE3ssP3k1fu8zsYbw5g3UPbSjAvQLdXkdD1qAWztXj7hc5Kxc4pYRyGM1_ljVOHg3Py_zSlYscnoNjCvRua2MDQgusCsEquNqGREFdvhjDkbeMhEFYxHucTnIn96OxIJEpamePTHsBooYyPBaa_ejGZ_C99QeDjpSkSKBgEe3aL1uWKlYhsGKh7biQUR5rKsKPodwccLIrW8Gr5tag3NH0sLPExHHvqzlpkj--KIuydTVjPH7u2zHxmPByServ2S5xjXYUBRr-ly3e1xPsVMhZZH9TxfttCIHLscBvpvCswIfaGYdl3bEzsrFISfpp0rpKtlp9gWGY7Tbk2n6s3etCHQEHn2qmM8bsJwkZV81pUWN0j9C9RX-ywOyIKY2yp1w_Iq1mRwOwY4mckbicOoooHiV6JER4xe7Kizw9hbXOnezn_NMk15TLwRoXlfL1s73uwogo-VWE8c-V1HqRpWQSyudRhLwhOEclrICXIdxICOgTgYO1z57xCEerw3QUL_7MPDrlbbh_AlX8I6Jfe8IhQ1Fkqu_njatm6aBTjkp2CSqlvZJpI_Lrv330VcyFEqBkGn7NJew3I9xofSrBaXFa8ABi6DXQm6-yC32OEyf7GHNXINjT1IB0yh6KR6c0qzaqiqOzKcuuai9XqEMQNNKyi6EuhzH5TP9YA56N3JhnXRFhs2aWHZhLlieVI6_uqzpZSgYjUem8aQrMTlmHw0kIYU8I-Ca041C4Zm2gMezwygRrhzsOoAmbmu96nft0KuIWTB3A_xGVKYQ2qjb2KRM7nsglnSEhDoNs8EhvuIm0FQs30YSCp5GhRO3b3Tn5rsLuwiWgu8hwEGhL0S1A"
    pagetoken = None
    placeList = ''

    while True:
        pagetoken, placeList = search_cuisine20(
            pagetoken=pagetoken, placeList=placeList)

        import time
        time.sleep(5)
        if not pagetoken:
            break

    return placeList