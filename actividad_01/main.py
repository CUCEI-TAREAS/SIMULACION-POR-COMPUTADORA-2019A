#!/usr/bin/env python

import sys

import gui_cartesian as plane
import gui_loadfile as files

if __name__ == "__main__":

    print(" starting ")

    file_selected = files.selectFile()

    points = list()

    if isinstance(file_selected, (str)):
        points = files.getListFromCSV(file_selected)

    print("from the main", points)
    plane.setupPlane(points)
