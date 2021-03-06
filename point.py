import math  # I am guessing that you will need to use the math module
import json  # I would like you to use the JSON module for reading geojson (for now)
from math import sqrt
from . import utils

class Point():
    def __init__(self, x=0, y=0, mark=[]):
        self.x = x
        self.y = y
        self.mark = mark
        
    def read_geojson(self,input_file):
        with open(input_file, 'r') as f:
            gj=json.load(f)
            
            # Please use the python json module (imported above)
            # to solve this one.
            
            return gj

    def check_if_coincident(self,secondPoint):
        return utils.check_coincident((self.x,self.y),secondPoint)
    
    def shiftPoint(self, x_shift, y_shift):
        return utils.shift_point((self.x,self.y),x_shift,y_shift)
    
    def shift_point(self,x_shift, y_shift):     
        self.x += x_shift
        self.y += y_shift    
        return self.x, self.y
    
def find_largest_city(gj):
    maximum=0;
    features=gj['features']
    
    for i in features:
        if (i['properties']['pop_max']>maximum):
            maximum=i['properties']['pop_max']
            city=i['properties']['nameascii']
    return city, maximum

def write_your_own(gj):
    #Calculate the number of citues with two-word names
    features=gj['features']
    count = 0
    for i in features:
        if(' ' in i['properties']['name']):
            count= count+1   
    
    return count

def mean_center(points):
    x_tot=0
    y_tot=0
    
    for i in points:
        x_tot+=i[0]
        y_tot+=i[1]
        
    x = x_tot/len(points)
    y = y_tot/len(points)

    return x, y

def average_nearest_neighbor_distance(points):
    mean_d = 0
    for i in points:
        dist_nearest=1e9
        for j in points:
            dist = euclidean_distance(i, j)
            if i==j:
                continue
            elif dist < dist_nearest:
                dist_nearest = dist;
        mean_d += dist_nearest;
    mean_d=mean_d/(len(points))
    return mean_d

def minimum_bounding_rectangle(points):
    #set initial params
    xmin=points[1][0]
    ymin=points[1][1]
    xmax=points[1][0]
    ymax=points[1][1]
    
    for i in points:
        curr_x=i[0]
        curr_y=i[1]
        if curr_x < xmin:
            xmin= curr_x 
        elif curr_x > xmax:
            xmax= curr_x
                
        if curr_y < ymin:
            ymin= curr_y 
        elif curr_y > ymax:
            ymax= curr_y 
    mbr = [xmin,ymin,xmax,ymax]

    return mbr

def mbr_area(mbr):
    return (mbr[3]-mbr[1])*(mbr[2]-mbr[0])

def expected_distance(area, n):
    return 0.5*(sqrt(area/n))

def manhattan_distance(a, b):
    distance =  abs(a[0] - b[0]) + abs(a[1] - b[1])
    return distance

def euclidean_distance(a, b):
    distance = math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)
    return distance

def shift_point(point, x_shift, y_shift):
    x = point
    y = gety(point)

    x += x_shift
    y += y_shift

    return x, y

def check_coincident(a, b):
    return a == b

def check_in(point, point_list):
    return point in point_list

def getx(point):
    return point[0]

def gety(point):
    return point[1]
