#!/usr/bin/env

import math

class Point:
    def __init__(self, lis=None, x=0, y=0):

       	if lis.any():
            self.x = int(x)
            self.y = int(y)
       	    return

        self.x = int(lis[0])
        self.y = int(lis[1])

	# TODO implement magic method to receive list of points
    def __eq__(self, x, y):
        self.x = int(x)
        self.y = int(y)
	


def distance_between_points(pointA, pointB):
    """ return the euclidean distance between 2 points """

    return math.sqrt(math.pow(( pointA.x - pointB.x), 2) + math.pow(( pointA.y - pointB.y), 2))
