import matplotlib.pyplot as plt
import numpy as np

def setupPlane(points=[]):
    fig, ax = plt.subplots()

    ax.axis('on', xscale='log', yscale='log', xmin=0, ymin=0, xmax=300, ymax=300, str="equal")
    #ax.axis(str="tight")

    #drawPoint(points, ax)

    ax.legend()
    ax.grid(True)
    plt.show()
    #mng = plt.get_current_fig_manager()
    #mng.frame.Maximize(True)


def drawPoint(points, ax):
    print(points)
    color=['red', 'green', 'blue']
    scale = 200
    for point in points:
        x = point[0]
        y = point[1]
        print(x, " valor ", y, " con respecto a ", point )

        ax.scatter(x, y, c=color[0], s=scale, alpha=0.3, edgecolors='face')


