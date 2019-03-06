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
    radius = pts.distance_between_points(center, curve)

    f = 1 - radius
    ddf_x = 1
    ddf_y = -2 * radius

    x = 0
    y = radius


    points = list()

    points.append(pts.Point(center.x, round(center.y + radius)))
    points.append(pts.Point(center.x, round(center.y - radius)))
    points.append(pts.Point(round(center.x + radius), center.y))
    points.append(pts.Point(round(center.x + radius), center.y))

    while x < y:
        if f >= 0: 
            y -= 1
            ddf_y += 2
            f += ddf_y
        x += 1
        ddf_x += 2
        f += ddf_x    
        points.append(pts.Point(round(center.x + x), round(center.y + y)))
        points.append(pts.Point(round(center.x - x), round(center.y + y)))
        points.append(pts.Point(round(center.x + x), round(center.y - y)))
        points.append(pts.Point(round(center.x - x), round(center.y - y)))
        points.append(pts.Point(round(center.x + y), round(center.y + x)))
        points.append(pts.Point(round(center.x - y), round(center.y + x)))
        points.append(pts.Point(round(center.x + y), round(center.y - x)))
        points.append(pts.Point(round(center.x - y), round(center.y - x)))


    return points




def dda_circle(center, curve):
    """ Draw a circle 

        Given two points draw a circle dda algorithm

        center: point for the center of the circle
        curve: point over the curve use as radius
        return: list of points representing the circle
    """

    radius = pts.distance_between_points(center, curve)

    radius_2 = radius * radius

    points = list()

    # for x 
    for x in range( int(center.x - radius), int(center.x + radius), 1 ):

        x2 = center.x - x
        x3 = x2 * x2

        y2 = abs( radius_2 - x3 )
        y = math.sqrt( y2 )

        points.append(pts.Point(x, center.y + y ))
        points.append(pts.Point(x, center.y - y ))

    # for y 
    for x in range( int(center.y - radius), int(center.y + radius), 1 ):

        x2 = center.y - x
        x3 = x2 * x2

        y2 = abs( radius_2 - x3 )
        y = math.sqrt( y2 )

        points.append(pts.Point(round(center.x + y), x ))
        points.append(pts.Point(round(center.x - y), x ))

    return points

