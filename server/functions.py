from collections import Counter
from scipy.spatial import ConvexHull, convex_hull_plot_2d
import numpy as np
from Profile import *

from firebaseClient import FirebaseClient, credit_cards
#def get_avg_spending_v1( , spending_arr):
#    # ex. spending_arr [[low1, high1], [low2, high2], [low3, high3]]
#    size = len(spending_arr)
#    low = 0.0
#    high = 0.0
#    for interval in spending_arr:
#        low = low + float(interval[0])
#        high = high + float(interval[1])
#    low = low / size
#    high = high / size
#    return [low, high]

def get_avg_spending_v2(arrayProfile):
    low_avg = arrayProfile[0].averageSpending
    high_avg = arrayProfile[0].averageSpending
    for profile in arrayProfile:
        if profile.averageSpending < low_avg:
            low_avg = profile.averageSpending
        if profile.averageSpending > high_avg:
            high_avg = profile.averageSpending

    # apply a sigmoid/exponential/some nonlinear function to find avg between the highest and lowest spenders
    # y = 1/(1+e^(-0.04x))
    diff = abs(high_avg - low_avg)
    proportion = 1-(1/(1+e**(-0.04*diff)))
    final = (diff * proportion) + low_avg
    return final

def get_popular_cuisine_v1( cuisine_pref, top):
    # ex. cuisine_pref [["Chinese", "French"], ["French", "Italian", "Brazilian"], ["French"]]
    array_total = [cuisine for tup in cuisine_pref for cuisine in tup]
    # for tup in cuisine_pref:
    #     for cuisine in tup:
    #         array_total.append(cuisine)
    return Counter(array_total).most_common(top)

def remove_location_outlier_v1(locations):
    # ex. locations [[coord_x, coord_y], [coord_x, coord_y]]
    # given a list of coordinates, remove outlier coordinates
    # use 2D 1.5 * IQR formula for outlier
    size = len(locations)
    half_size = int(size / 2)
    x = []
    y = []
    for coord in locations:
        x.append(coord[0])
        y.append(coord[1])
    first_q_x = np.median(x[half_size:])
    third_q_x = np.median(x[:half_size])
    first_q_y = np.median(y[half_size:])
    third_q_y = np.median(y[:half_size])
    interq_range_x = third_q_x - first_q_x
    interq_range_y = third_q_y - first_q_y

    # most extreme values allowed
    val = 15
    x_min = first_q_x - (val * interq_range_x)
    x_max = third_q_x + (val * interq_range_x)
    y_min = first_q_y - (val * interq_range_y)
    y_max = third_q_y + (val * interq_range_y)
    
    # filter
    #print(x_min, x_max, y_min, y_max)
    #print("locations size is 1) "+str(len(locations)))
    locations_filtered = []
    for entry in locations:
        # print(locations[i][0])
        x = abs(entry[0])
        y = abs(entry[1])
    # locations = [x for x in locations if not determine(x, x_max, x_min, y_max, y_min)]
        if x < abs(x_max) and x > abs(x_min) and y < abs(y_max) and y > abs(y_min):
            if entry not in locations_filtered:
                locations_filtered.append(entry)
        #     i = max(0, i - 1)
    #print(len(locations))
    #print("locations size is 2) "+str(len(locations_filtered)))
    #print(locations_filtered)
    return locations_filtered

def determine(val, x_max, x_min, y_min, y_max):
    x = val[0]
    y = val[1]
    if x > x_max or x < x_min or y > y_max or y < y_min:
        return False
    return True

def get_possible_location_v1(locations_eaten):
    # average location (geometric mean)
    # ex. locations_eaten [[x_coord, y_coord], [3.1, 4.5], [8.8, 9.5]]
    locations_eaten = remove_location_outlier_v1(locations_eaten)

    size = len(locations_eaten)
    x = 0.0
    y = 0.0
    for coord in spending_arr:
        x = x + float(coord[0])
        y = y + float(coord[1])
    x = x / size
    y = y / size
    return [x, y]

def get_possible_location_v2(locations):
    # low cost transportation (geometric median method)
    # convex hull intersect geo median circle
    # return a convex hull of area to search for food
    
    locations = remove_location_outlier_v1(locations)

    # can't make convex hull with 2 or less points
    if len(locations) < 3:
        return []

    points = np.array(locations)
    hull = ConvexHull(points)
    # hull.vertices gives INDICES of points on the convex hull

    ret = []
    for ind in hull.vertices:
        ret.append(hull.points[ind])
    
    cx = np.mean(hull.points[hull.vertices,0])
    cy = np.mean(hull.points[hull.vertices,1])
    
    return (ret, [cx, cy])

def get_possible_location_v3( locations_eaten):
    # likely will not implement
    # step 1: remove users that are too far away
    remove_location_outlier_v1(locations_eaten)
    # step 2: smallest enclosing circle using Welzl's algorithm

    pass
    
def point_inside_hull_v1(point, hull):
    if not isinstance(hull,ConvexHull):
        return False
    
    return hull.find_simplex(point) >= 0
        
