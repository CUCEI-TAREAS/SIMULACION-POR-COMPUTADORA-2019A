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

        y = float(math.sqrt( (rx2ry2 - (float( x ** 2) * ry2)) / float(rx2)))

        points.append(pts.Point(center.x + x, center.y + y ))
        points.append(pts.Point(center.x + x, center.y - y ))
        points.append(pts.Point(center.x - x, center.y + y ))
        points.append(pts.Point(center.x - x, center.y - y ))


    for y in range(int(ry)):

        x = float(math.sqrt( (rx2ry2 - (float(y ** 2) * rx2)) / float(ry2)))

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

    rx = get_axis_x(curve, center)
    ry = get_axis_y(curve, center)

    points = list()

    x = float(0)
    y = float(ry)

    rx2 = float(rx ** 2)
    ry2 = float(ry ** 2)

    pk = ry2 - (rx2 * ry) + (0.25 * rx2)

    while (2 * ry2 * x) <= (2 * rx2 * y):

        points.append(pts.Point(center.x + x, center.y + y ))
        points.append(pts.Point(center.x + x, center.y - y ))
        points.append(pts.Point(center.x - x, center.y + y ))
        points.append(pts.Point(center.x - x, center.y - y ))

        if pk < 0:
            x += 1
            pk = pk + (2 * ry2 * x) + ry2
        else:
            x += 1
            y -= 1
            #pk = pk + (2 * ry2 * x) - (2 * rx2 * y) + ry2
            pk = pk + (2 * ry2 * x + ry2 ) - (2 * rx2 * y)
        

    pk2 = float(x + 0.5) * float( x + 0.5 ) * ry2 + (y - 1) * ( y - 1) * rx2 - rx2 * ry2

    while y >= 0:

        points.append(pts.Point(center.x + x, center.y + y ))
        points.append(pts.Point(center.x + x, center.y - y ))
        points.append(pts.Point(center.x - x, center.y + y ))
        points.append(pts.Point(center.x - x, center.y - y ))

        if pk2 > 0:
            y -= 1
            pk2 = pk2 - (2 * rx2 * y) + rx2
        else:
            x += 1
            y -= 1
            pk2 = pk2 + (2 * ry2 * x) - (2 * rx2 * y) + rx2
    

    return points

