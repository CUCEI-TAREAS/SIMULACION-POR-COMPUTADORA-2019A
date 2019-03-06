#!/usr/bin/env

import math

class Point:

    # TODO implement magic method to receive list of points
    def __init__(self, x=0, y=0):
        self.x = int(x)
        self.y = int(y)


    def __str__(self):
        return "x: " + str(self.x)+ " y: " + str(self.y)

    def __eq__(self, pointb):
        return self.x == pointb.x and self.y == pointb.y
	


def distance_between_points(pointA, pointB):
    """ return the euclidean distance between 2 points """

    return math.sqrt(math.pow(( pointA.x - pointB.x), 2) + math.pow(( pointA.y - pointB.y), 2))
