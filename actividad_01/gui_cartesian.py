import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

def onclick(event):
    print(event.button, event.xdata, event.ydata)

    if event.button == 3:
        drawPoint([[int(event.xdata), int(event.ydata)]])

def setupPlane(points=[]):
    plt.plot(range(300), linewidth=1.0)
    plt.grid()

    fig.canvas.mpl_connect('button_press_event', onclick)
    ax.legend()
    drawPoint(points)
    plt.show()

def drawPoint(points=[]):
    color=['red', 'green', 'blue']
    scale = 100
    for point in points:
        x = point[0]
        y = point[1]
        print(x, " valor ", y, " con respecto a ", point )

        ax.scatter(int(x), int(y), c=color[0], s=scale, alpha=0.3, edgecolors='face')

    plt.show()
