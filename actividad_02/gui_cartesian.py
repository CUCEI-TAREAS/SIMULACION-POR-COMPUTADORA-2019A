import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

final_points = list()

def onclick(event):
    print(event.button, event.xdata, event.ydata)

    if event.button == 3:
        #drawPoint([[int(event.xdata), int(event.ydata)]])
        dda(int(event.xdata), int(event.ydata), 0, 0)


def setupPlane():

    plt.plot(range(300), linewidth=0)
    plt.grid()

    fig.canvas.mpl_connect('button_press_event', onclick)

    ax.legend()

    plt.show()

def drawPoint(points=[]):
    color=['red', 'green', 'blue']
    scale = 10
    for point in points:
        x = point[0]
        y = point[1]
        print(x, " valor ", y, " con respecto a ", point )

        ax.scatter(int(x), int(y), c=color[0], s=scale, alpha=0.3, edgecolors='face')



def dda(xi, yi, xf, yf):

    inc = 1

    m = (yf - yi) / (xf - xi)
    b = yi - (m * xi)

    if m > 1 :
        if yf < yi :
            inc = -1

        for i in range(yi, yf, inc):
            yact = m * i + b
            drawPoint([[i, yact]])
    else:
        if xi > xf :
            inc = -1

        for i in range(xi, xf, inc):
            yact = m * i + b
            drawPoint([[i, yact]])

    plt.show()
