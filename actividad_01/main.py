#!/usr/bin/env python

import sys

import gui_cartesian as plane
import gui_loadfile as files

if __name__ == "__main__":

    print(" starting ")

    file_selected = files.selectFile()
    points = files.getListFromCSV(file_selected)
    plane.setupPlane(points)
