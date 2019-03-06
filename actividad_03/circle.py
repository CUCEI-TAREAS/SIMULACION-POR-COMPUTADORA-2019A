import math

import points as pts
import plane

def bresenham_circle(center, curve):
    """ Draw a circle 

        Given two points draw a circle with bresenham algorithm

        center: point for the center of the circle
        curve: point over the curve use as radius
        return: list of points representing the circle
    """
    radius = int(pts.distance_between_points(center, curve))

    f = 1 - radius
    ddf_x = 1
    ddf_y = -2 * radius

    x = 0
    y = radius


    points = list()
	
    points.append(pts.Point(center.x, center.y + radius))
    points.append(pts.Point(center.x, center.y - radius))
    points.append(pts.Point(center.x + radius, center.y))
    points.append(pts.Point(center.x - radius, center.y))

    points.append(pts.Point(center.x, center.y - radius))
    points.append(pts.Point(center.x + radius, center.y))
    points.append(pts.Point(center.x - radius, center.y))

    while x < y:
        if f >= 0: 
            y -= 1
            ddf_y += 2
            f += ddf_y
        x += 1
        ddf_x += 2
        f += ddf_x    
        points.append(pts.Point(center.x + x, center.y + y))
        points.append(pts.Point(center.x - x, center.y + y))
        points.append(pts.Point(center.x + x, center.y - y))
        points.append(pts.Point(center.x - x, center.y - y))
        points.append(pts.Point(center.x + y, center.y + x))
        points.append(pts.Point(center.x - y, center.y + x))
        points.append(pts.Point(center.x + y, center.y - x))
        points.append(pts.Point(center.x - y, center.y - x))

	
    return points




def dda_circle(center, curve):
    """ Draw a circle 

        Given two points draw a circle dda algorithm

        center: point for the center of the circle
        curve: point over the curve use as radius
        return: list of points representing the circle
    """

    radius = pts.distance_between_points(center, curve)

    f = 1 - radius
    ddf_x = 1
    ddf_y = -2 * radius

    x = 0
    y = radius


    points = list()
	
    points.append(pts.Point(center.x, center.y + radius))
    points.append(pts.Point(center.x, center.y - radius))
    points.append(pts.Point(center.x + radius, center.y))
    points.append(pts.Point(center.x - radius, center.y))

    points.append(pts.Point(center.x, center.y - radius))
    points.append(pts.Point(center.x + radius, center.y))
    points.append(pts.Point(center.x - radius, center.y))
 
    while x < y:
        if f >= 0: 
            y -= 1
            ddf_y += 2
            f += ddf_y
        x += 1
        ddf_x += 2
        f += ddf_x    
        points.append(pts.Point(center.x + x, center.y + y))
        points.append(pts.Point(center.x - x, center.y + y))
        points.append(pts.Point(center.x + x, center.y - y))
        points.append(pts.Point(center.x - x, center.y - y))
        points.append(pts.Point(center.x + y, center.y + x))
        points.append(pts.Point(center.x - y, center.y + x))
        points.append(pts.Point(center.x + y, center.y - x))
        points.append(pts.Point(center.x - y, center.y - x))

	
    return points



