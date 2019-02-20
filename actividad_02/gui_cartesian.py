import datetime
import matplotlib.pyplot as plt
import numpy as np

from matplotlib.image import AxesImage

fig, ax = plt.subplots()

final_points = list()

def onclick(event):

    if event.button == 3:
        print(int(round(event.xdata)), int(round(event.ydata)))

        if final_points == []:
            final_points.append([int(round(event.xdata)), int(round(event.ydata))])
        else:
            dda(final_points[0][0], final_points[0][1], int(round(event.xdata)), int(round(event.ydata)))

def setupPlane():

    plt.plot(range(0, 300), linewidth=0)
    #ax.axis=([0, 300, 0, 300])

    plt.grid()

    fig.canvas.mpl_connect('button_press_event', onclick)

    ax.legend()

    plt.show()

def drawPoint(points=[], col=0):
    color=['red', 'green', 'blue']
    scale = 10
    for point in points:
        x = point[0]
        y = point[1]
        #print(x, " valor ", y, " con respecto a ", point )

        ax.scatter(int(x), int(y), c=color[col], s=scale, alpha=0.3, edgecolors='face')
        #im1 = ax.imshow(rand(10, 5), extent=(1, 2, 1, 2), picker=True)



def dda(xi, yi, xf, yf):

    dda_time_inicio = datetime.datetime.now()

    ordenada = False
    absisa = False
    t = 0

    inc = 1

    dy = yf - yi
    dx = xf - xi

    m = 0

    if dy == 0:
        t += 1
        absisa = True

    if dx == 0:
        t += 1
        ordenada = True

    if t == 2:
        print("error, same point")
        final_points.clear()
        return -1

    if t != 1:
        m = dy / dx

    b = yi - (m * xi)

    if ordenada:

        if yi > yf :
            inc = -1
            b = yf

        for i in range(yi, yf, inc):
            yact = b
            drawPoint([[round(yact), i]], 2)
            #print("from ordenada") elif absisa:

        if xi > xf :
            inc = -1
            b = yf

        for i in range(xi, xf, inc):
            yact = b
            drawPoint([i, [round(yact)]], 2)
            #print("from absisa")

    elif m >= 1:

        if yi > yf :
            inc = -1

        for i in range(yi, yf, inc):
            yact = (i - b) / m
            drawPoint([[round(yact), i]], 2)
            #print("from m >= 1")

    elif m > -1 :
        if xi > xf :
            inc = -1

        for i in range(xi, xf, inc):
            yact = ( m * i) + b
            drawPoint([[i, round(yact)]], 2)
            #print("from m > 0")

    elif m <= -1 :
        if yi > yf :
            inc = -1

        for i in range(yi, yf, inc):
            yact = (i - b) / m
            drawPoint([[round(yact),i]], 2)
            #print("from m >= -1")


    #print(m)
    final_points.clear()
    dda_time_end = datetime.datetime.now()
    dda_time = dda_time_inicio - dda_time_end
    print("TIME EXECUTION FOR DDA :",dda_time.seconds, "SECONDS AND ", dda_time.microseconds, "MICROSECONDS")
    plt.show()

def bresenham(xi, yi, xf, yf):
