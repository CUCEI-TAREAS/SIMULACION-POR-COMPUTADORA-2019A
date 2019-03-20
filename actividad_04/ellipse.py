import math

import points as pts

def get_axis_y(center, axes):
    """ Get the axes y"""

    return float(abs(center.y - axes.y))


def get_axis_x(center, axes):
    """ Get the axes x"""

    return float(abs(center.x - axes.x))


def dda_ellipse(center, curve):
    """ Draw a ellipse 

        Given two points draw a ellipse with bresenham algorithm

        center: point for the center of the ellipse
        curve: point over the curve use as radius
        return: list of points representing the ellipse
    """

    rx = get_axis_x(curve, center)
    ry = get_axis_y(curve, center)

    points = list()

    rx2 = float(rx ** 2)
    ry2 = float(ry ** 2)

    rx2ry2 = float(rx2 * ry2)

    for x in range(int(rx)):

        y = float(math.sqrt( (rx2ry2 - (float(x**2) * ry2)) / float(rx2)))

        points.append(pts.Point(center.x + x, center.y + y ))
        points.append(pts.Point(center.x + x, center.y - y ))
        points.append(pts.Point(center.x - x, center.y + y ))
        points.append(pts.Point(center.x - x, center.y - y ))


    for y in range(int(ry)):

        x = float(math.sqrt( (rx2ry2 - (float(y**2) * rx2)) / float(ry2)))

        points.append(pts.Point(center.x + x, center.y + y ))
        points.append(pts.Point(center.x + x, center.y - y ))
        points.append(pts.Point(center.x - x, center.y + y ))
        points.append(pts.Point(center.x - x, center.y - y ))


    return points

def bresenham_ellipse(center, curve):
    """ Draw a ellipse 

        Given two points draw a ellipse dda algorithm

        center: point for the center of the ellipse
        curve: point over the curve use as radius
        return: list of points representing the ellipse
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

