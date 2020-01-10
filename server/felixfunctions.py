from collections import Counter
from scipy.spatial import ConvexHull, convex_hull_plot_2d
import numpy as np
from Profile import *
import math
from matplotlib.path import Path
from bisect import bisect_left 

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

# Law of Haversine???
def measure(lat1, lon1, lat2, lon2):  # generally used geo measurement function
    R = 6378.137; # Radius of earth in KM 
    dLat = lat2 * math.pi / 180.0 - lat1 * math.pi / 180.0
    dLon = lon2 * math.pi / 180.0 - lon1 * math.pi / 180.0
    a = math.sin(dLat/2.0) * math.sin(dLat/2.0) + math.cos(lat1 * math.pi / 180.0) * math.cos(lat2 * math.pi / 180.0) * math.sin(dLon/2.0) * math.sin(dLon/2.0)
    c = 2.0 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = R * c
    return d * 1000.0; # meters

def get_coords_from_trans(tot_trans):
    # tot_trans: [[a,b], [c,d], ...]
    coords = []
    #file = open("testfile1.txt","w") 
    for entry in tot_trans:
        coords.append(entry['coordinates'])
        #file.write(str(entry['coordinates'][0]) + ","+str(entry['coordinates'][1])+"\n")

    #file.close()
    # print(coords)
    return coords

def final_area(tot_trans):
    coords = get_coords_from_trans(tot_trans)
    hull = get_possible_location_v2(coords)

    #file = open("testfile2.txt","w") 
    longest_dist = 0.0
    w = -1
    x = -1
    y = -1
    z = -1
    #print(hull)
    if not hull:
        return ([], [38.909, -77.031], 1000, NULL)

    for entry in hull[0]:
        #file.write(str(entry[0]) + ","+str(entry[1])+"\n")
        d = measure(hull[1][0], hull[1][1], entry[0], entry[1]) 
        if d > longest_dist:
            longest_dist = d
            w = hull[1][0]
            x = hull[1][1]
            y = entry[0]
            z = entry[1]
    #file.write(str(hull[1][0]) + ","+str(hull[1][1]))
    #print("%f, %f and %f, %f has distance: %s" % (w,x,y,z,str(d)))
    #file.close()
    # ret, centroid, ConvexHull
    return (hull[0], hull[1], d, hull[2])

def int_to_dollars(i):
    return i * 10

def BinarySearch(a, x): 
    i = bisect_left(a, x) 
    if i: 
        return (i-1) 
    else: 
        return -1

def priority_rest_by_rewards(restaurants, user):
    restaurants = sorted(restaurants, key=lambda shop: shop["price_level"])
    target = user['median_spending']/10
    i = BinarySearch(restaurants, target)
    return restaurants[0:i]

def get_avg_spending_v2(arrayProfile):
    low_avg = arrayProfile[0]["averageSpending"]
    high_avg = arrayProfile[0]["averageSpending"]
    for profile in arrayProfile:
        if profile["averageSpending"] < low_avg:
            low_avg = profile["averageSpending"]
        if profile["averageSpending"] > high_avg:
            high_avg = profile["averageSpending"]

    # apply a sigmoid/exponential/some nonlinear function to find avg between the highest and lowest spenders
    # y = 1/(1+e^(-0.04x))
    diff = abs(high_avg - low_avg)
    proportion = 1-(1/(1+math.e**(-0.04*diff)))
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
    val = 20
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
        x = entry[0]
        y = entry[1]
        
        interval_x = [min(x_max, x_min), max(x_max, x_min)]
        interval_y = [min(y_max, y_min), max(y_max, y_min)]
    # locations = [x for x in locations if not determine(x, x_max, x_min, y_max, y_min)]
        if x >= interval_x[0] and x <= interval_x[1] and y >= interval_y[0] and y <= interval_y[1]:
            if entry not in locations_filtered:
                locations_filtered.append(entry)
        #     i = max(0, i - 1)
    #print(len(locations))
    #print("locations size is 2) "+str(len(locations_filtered)))
    #print(locations_filtered)
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
    #print(locations)
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
    
    return (ret, [cx, cy], hull)

def get_possible_location_v3( locations_eaten):
    # likely will not implement
    # step 1: remove users that are too far away
    remove_location_outlier_v1(locations_eaten)
    # step 2: smallest enclosing circle using Welzl's algorithm

    pass
    
def point_inside_hull_v1(point, hull):
    if not isinstance(hull,ConvexHull):
        return False
    hull_path = Path( hull.points[hull.vertices] )
    return hull_path.contains_point((point[0],point[1]))