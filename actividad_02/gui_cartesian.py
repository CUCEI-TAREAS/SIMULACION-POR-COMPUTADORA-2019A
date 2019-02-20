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
            x = final_points[0][0]
            y = final_points[0][1]

            bresenham(x, y, int(round(event.xdata)), int(round(event.ydata)))
            dda(x, y, int(round(event.xdata)), int(round(event.ydata)))

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

        ax.scatter(int(x), int(y), c=color[col], s=scale, alpha=0.2, edgecolors='face')
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
    #print("TIME DIFF BRESENHAN - DDA :", bres_time.seconds - dda_time.seconds, "SECONDS AND ", bres_time.microseconds - dda_time.microseconds, "MICROSECONDS")
    plt.show()


def bresenham(xi, yi, xf, yf):

    bres_time_inicio = datetime.datetime.now()

    dx = abs(xf - xi)
    dy = abs(yf - yi)
    x, y = xi, yi
    sx = -1 if xi > xf else 1
    sy = -1 if yi > yf else 1
    if dx > dy:
        err = dx / 2.0
        while x != xf:
            drawPoint([[x,y]],0)
            err -= dy
            if err < 0:
                y += sy
                err += dx
            x += sx
    else:
        err = dy / 2.0
        while y != yf:
            drawPoint([[x,y]],0)
            err -= dx
            if err < 0:
                x += sx
                err += dy
            y += sy        

    drawPoint([[x,y]],0)

    bres_time_end = datetime.datetime.now()
    bres_time = bres_time_inicio - bres_time_end
    print("TIME EXECUTION FOR BRESENHAN :", bres_time.seconds, "SECONDS AND ", bres_time.microseconds, "MICROSECONDS")

