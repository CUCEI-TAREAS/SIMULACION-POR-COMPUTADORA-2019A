import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

def onclick(event):
    print(event.xdata, event.ydata)
    drawPoint([[int(event.xdata), int(event.ydata)]])

def setupPlane(points=[]):
    #ax.plot(range(300))
    #ax.axis('on', xscale='log', yscale='log', xmin=0, ymin=0, xmax=300, ymax=300, str="equal")
    fig.canvas.mpl_connect('button_press_event', onclick)
    drawPoint(points)

    #mng = plt.get_current_fig_manager()
    #mng.frame.Maximize(True)


def drawPoint(points):
    print(points)
    color=['red', 'green', 'blue']
    scale = 200
    for point in points:
        x = point[0]
        y = point[1]
        print(x, " valor ", y, " con respecto a ", point )

        ax.scatter(x, y, c=color[0], s=scale, alpha=0.3, edgecolors='face')

    ax.legend()
    ax.grid(True)
    plt.show()
