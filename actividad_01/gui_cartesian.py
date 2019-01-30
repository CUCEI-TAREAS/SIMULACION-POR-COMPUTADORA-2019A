import gui_loadfile as files

import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

final_points = list()

def onclick(event):
    print(event.button, event.xdata, event.ydata)

    if event.button == 3:
        drawPoint([[int(event.xdata), int(event.ydata)]])
        relativePoints(final_points)

def setupPlane(points=[]):

    plt.plot(range(300), linewidth=0)
    plt.grid()

    fig.canvas.mpl_connect('button_press_event', onclick)

    ax.legend()
    drawPoint(points)
    relativePoints(final_points)

    plt.show()

    files.writeCSVFrom(final_points, "points_final")
    files.writeCSVFrom(relativePoints(final_points), "valores_relativos")

def drawPoint(points=[]):
    color=['red', 'green', 'blue']
    scale = 100
    for point in points:
        x = point[0]
        y = point[1]
        print(x, " valor ", y, " con respecto a ", point )
        final_points.append([int(x), int(y)])
        relativePoints(final_points)

        ax.scatter(int(x), int(y), c=color[0], s=scale, alpha=0.3, edgecolors='face')

    plt.show()


def relativePoints(final_points):

    aux_x = final_points[0][0]
    aux_y = final_points[0][1]

    aux2_x = aux_x * -1
    aux2_y = aux_y * -1

    rel = list()
    rel.append(final_points[0])

    for point in final_points[1:]:
        aux_x = point[0] + aux2_x
        aux_y = point[1] + aux2_y

        rel.append([aux_x, aux_y])

        aux2_x -= aux_x
        aux2_y -= aux_y

    print("VALORES RELATIVOS: ", rel)
    return rel
