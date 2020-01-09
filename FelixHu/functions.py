from collections import Counter
from scipy.spatial import ConvexHull, convex_hull_plot_2d
import numpy as np

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

def get_avg_spending_v2(self, spending_arr):
    # get customers with lowest and highest spending averages
    lowest_ind = 0
    highest_ind = 0
    low_avg = float(spending_arr[0][0]+spending_arr[0][1])/2.0
    high_avg = float(spending_arr[0][0]+spending_arr[0][1])/2.0
    for i in range(1, len(spending_arr)):
        avg = float(spending_arr[i][0]+spending_arr[i][1])/2.0
        if avg < low_avg:
            low_avg = avg
            lowest_ind = i
        if avg > high_avg:
            high_avg = avg
            highest_ind = i

    # apply a sigmoid/exponential/some nonlinear function to find avg between the highest and lowest spenders
    # y = 1/(1+e^(-0.04x))

    diff = abs(high_avg - low_avg)
    proportion = 1-(1/(1+e**(-0.04*diff)))
    final = diff * proportion + low_avg
    return final

def get_popular_cuisine_v1(self, cuisine_pref, top):
    # ex. cuisine_pref [["Chinese", "French"], ["French", "Italian", "Brazilian"], ["French"]]
    array_total = [cuisine for tup in cuisine_pref for cuisine in tup]
    # for tup in cuisine_pref:
    #     for cuisine in tup:
    #         array_total.append(cuisine)
    return Counter(array_total).most_common(top)

def remove_location_outlier_v1(self, locations):
    # ex. locations [[coord_x, coord_y], [coord_x, coord_y]]
    # given a list of coordinates, remove outlier coordinates
    # use 2D 1.5 * IQR formula for outlier
    size = len(locations)
    half_size = size / 2
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
    x_min = first_q_x - 1.5 * interq_range_x
    x_max = third_q_x + 1.5 * interq_range_x
    y_min = first_q_y - 1.5 * interq_range_y
    y_max = third_q_y + 1.5 * interq_range_y

    # filter
    for i in range(0, len(locations)):
        x = locations[i][0]
        y = locations[i][1]
        if x > x_max or x < x_min or y > y_max or y < y_min:
            del locations[i]
            i = i - 1

def get_possible_location_v1(self, locations_eaten):
    # average location (geometric mean)
    # ex. locations_eaten [[x_coord, y_coord], [3.1, 4.5], [8.8, 9.5]]
    remove_location_outlier_v1(locations_eaten)

    size = len(locations_eaten)
    x = 0.0
    y = 0.0
    for coord in spending_arr:
        x = x + float(coord[0])
        y = y + float(coord[1])
    x = x / size
    y = y / size
    return [x, y]

def get_possible_location_v2(self, locations):
    # low cost transportation (geometric median method)
    # convex hull intersect geo median circle
    # return a convex hull of area to search for food
    
    remove_location_outlier_v1(locations_eaten)

    points = np.array(locations)
    hull = ConvexHull(points)
    # hull.vertices gives INDICES of points on the convex hull

    ret = []
    for ind in hull.vertices:
        ret.append(hull.points[ind])
    
    return ret

def get_possible_location_v3(self, locations_eaten):
    # likely will not implement
    # step 1: remove users that are too far away
    remove_location_outlier_v1(locations_eaten)
    # step 2: smallest enclosing circle using Welzl's algorithm

    pass
    
def point_inside_hull_v1(self, point, hull):
    if not isinstance(hull,ConvexHull):
        return False
    
    return hull.find_simplex(point) >= 0
        
