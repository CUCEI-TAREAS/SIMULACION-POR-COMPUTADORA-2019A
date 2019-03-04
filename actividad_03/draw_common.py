import gui_cartesian as gui

def drawPoint(points=[], col=0):
    color=['red', 'green', 'blue']
    scale = 10

    for point in points:
        x = point[0]
        y = point[1]
        print(x, " valor ", y, " con respecto a ", point )

        gui.ax.scatter(int(x), int(y), c=color[col], s=scale, alpha=0.2, edgecolors='face')

