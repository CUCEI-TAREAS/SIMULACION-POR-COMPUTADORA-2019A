#!/usr/bin/env

import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = int(x)
        self.y = int(y)


	# TODO implement magic method to receive list of points
    def __eq__(self, x, y):
        self.x = int(x)
        self.y = int(y)
	


def distance_between_points(pointA, pointB):
    """ return the euclidean distance between 2 points """

    return math.sqrt(math.pow(( pointA.x - pointB.x), 2) + math.pow(( pointA.y - pointB.y), 2))
