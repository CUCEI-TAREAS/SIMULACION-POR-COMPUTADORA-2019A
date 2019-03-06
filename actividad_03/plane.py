#!/usr/bin/env

import sys

import matplotlib.pyplot as plt

from points import Point

class Plane:

    # TODO: implement features with kwargs
    def __init__(self, fname=None, **kwargs):


        if kwargs:
            with plt.rc_context(rc=kwargs):
                self.fig, self.ax = plt.subplots()
                plt.show()

        else:
            self.fig, self.ax = plt.subplots()
            plt.show()

    # euclidean distance
    def distance(PointA, PointB):
         return math.sqrt(math.pow(( PointA.x - PointB.x), 2) + math.pow(( PointA.y - PointB.y), 2))

