import math
import numpy as np
from numpy import ones,vstack
from numpy.linalg import lstsq

###################################
######  work in progress   ########
###################################

# point passed be list,tuple


def mid_point_between_points(point1,point2):
    mid_point_x = (point1[0]+point2[0])/2
    mid_point_y = (point1[1]+point2[1])/2
    return [mid_point_x, mid_point_y]

def slope_between_points(point1,point2):
    if point1[0] == point2[0]:
        return np.inf
    else:
        m = (point2[1] - point1[1]) / (point2[0] - point1[0])
        return m

def distance_between_points(point1, point2,refrance_axis):
    if refrance_axis == "x":
        return math.sqrt((point1[0]-point2[0])**2)
    if refrance_axis == "y":
        return math.sqrt((point1[1]-point2[1])**2)
    if refrance_axis == "xy":
        return math.sqrt((point1[0]-point2[0])**2+(point1[1]-point2[1])**2)

def equation_of_line(point1,point2):

    points = [point1,point2]
    x_coords, y_coords = zip(*points)
    A = vstack([x_coords,ones(len(x_coords))]).T
    m, c = lstsq(A, y_coords)[0]
    return "y={m}x + {c}".format(m=m, c=c), m, c