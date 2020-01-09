from collections import Counter

def get_avg_spending_v1(self, spending_arr):
    # ex. spending_arr [[low1, high1], [low2, high2], [low3, high3]]
    size = len(spending_arr)
    low = 0.0
    high = 0.0
    for interval in spending_arr:
        low = low + float(interval[0])
        high = high + float(interval[1])
    low = low / size
    high = high / size
    return [low, high]

def get_popular_cuisine_v1(self, cuisine_pref, top):
    # ex. cuisine_pref [["Chinese", "French"], ["French", "Italian", "Brazilian"], ["French"]]
    array_total = [cuisine for tup in cuisine_pref for cuisine in tup]
    # for tup in cuisine_pref:
    #     for cuisine in tup:
    #         array_total.append(cuisine)
    return Counter(array_total).most_common(top)

def get_possible_location_v1(self, locations_eaten):
    # average location (geometric mean)
    # ex. locations_eaten [[x_coord, y_coord], [3.1, 4.5], [8.8, 9.5]]
    size = len(locations_eaten)
    x = 0.0
    y = 0.0
    for coord in spending_arr:
        x = x + float(coord[0])
        y = y + float(coord[1])
    x = x / size
    y = y / size
    return [x, y]

def get_possible_location_v2(self, locations_eaten):
    # low cost transportation (geometric median method)
    

def get_possible_location_v3(self, locations_eaten):
    # step 1: remove users that are too far away

    # step 2: smallest enclosing circle using Welzl's algorithm


    pass
    
