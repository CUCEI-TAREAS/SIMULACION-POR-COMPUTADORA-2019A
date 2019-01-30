#!/usr/bin/env python

import csv

from tkinter import Tk
from tkinter.filedialog import askopenfilename

def selectFile():
    root = Tk()
    root.withdraw() # we don't want a full GUI, so keep the root window from appearing
    filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
    root.destroy()
    return filename

def getListFromCSV(path):
    print(path)
    points = list()
    with open(path, "r") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            points.append(row)

    return points

