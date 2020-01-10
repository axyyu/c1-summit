from functions import *
from firebaseClient import FirebaseClient
import math

def main():
    fb = FirebaseClient()
    
    tot_trans = []
    tot_trans_2 = []
    db = fb.db
    temp = db.collection('users').stream()
    for doc in temp:
        trans = db.collection('users').document(doc.id).collection('transactions').stream()
        tot_trans_2.append(doc.to_dict())
        for x in trans:
            tot_trans.append(x.to_dict())
    # print(tot_trans[0])
    stuff2(tot_trans_2)
    
def stuff2(tot_trans):
    #print(tot_trans)
    ret = get_avg_spending_v2(tot_trans)
    print(ret)

def stuff1(tot_trans):
    coords = get_coords_from_trans(tot_trans)

    hull = get_possible_location_v2(coords)

    #print(hull)
    file = open("testfile2.txt","w") 
    longest_dist = 0.0
    w = -1
    x = -1
    y = -1
    z = -1
    for entry in hull[0]:
        file.write(str(entry[0]) + ","+str(entry[1])+"\n")
        d = measure(hull[1][0], hull[1][1], entry[0], entry[1]) 
        if d > longest_dist:
            longest_dist = d
            w = hull[1][0]
            x = hull[1][1]
            y = entry[0]
            z = entry[1]
    file.write(str(hull[1][0]) + ","+str(hull[1][1]))
    print("%f, %f and %f, %f has distance: %s" % (w,x,y,z,str(d)))
    file.close()

def dist(a, b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

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
    coords = []
    file = open("testfile1.txt","w") 
    for entry in tot_trans:
        coords.append(entry['coordinates'])
        file.write(str(entry['coordinates'][0]) + ","+str(entry['coordinates'][1])+"\n")

    file.close()
    # print(coords)
    return coords

if __name__== "__main__":
  main()