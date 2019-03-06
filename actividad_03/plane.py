#!/usr/bin/env

import sys
import math

import matplotlib.pyplot as plt
import numpy as np

import points as pts
import circle

class Plane:

    # TODO: implement features with kwargs
    def __init__(self, points=None,fname=None, **kwargs):

        if not points:
            self.points = []

        else:
            self.points = points

        if not kwargs:
            with plt.rc_context(rc=kwargs):
                self.fig, self.ax = plt.subplots()

        else:
            self.fig, self.ax = plt.subplots()

    def right_click(self, event):
        if event.button == 3:
            # TODO unstable:  implement correct way to clean
            plt.cla()
            self.start()
            print('click')

    
	# TODO implement features with kwargs
    def start(self):
        plt.ion()
        plt.title("DDA & BRESENHAM CIRCLE", fontsize=16)
        plt.plot(range(0, 300), linewidth=0)
        plt.axis("equal")
        plt.grid(True)

        self.fig.canvas.mpl_connect('button_press_event', self.right_click)
        self.ax.legend()

        while(True):

            plt.draw()

            a, b =  np.asarray(plt.ginput(2, timeout=-1))

            c = pts.Point(a[0], a[1])
            r = pts.Point(b[0], b[1])

            self.drawPoint(_points=c, color="purple", scale=40, alpha=.9)
            self.drawPoint(_points=r, color="black", scale=40, alpha=.9)

            self.drawPoint(circle.bresenham_circle(c, r))
            self.drawPoint(circle.dda_circle(c, r), color='green')
            #plt.waitforbuttonpress()


    def drawPoint(self, _points=None, color='blue', scale=10, alpha=0.2):

        if isinstance(_points, list):

            for point in _points:
                self.ax.scatter(point.x, point.y, c=color, s=scale, alpha=0.2, edgecolors='face')
                self.points.append(point)

        else:

            self.ax.scatter(_points.x, _points.y, c=color, s=scale, alpha=0.2, edgecolors='face')
            self.points.append(_points)

