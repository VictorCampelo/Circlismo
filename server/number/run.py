# -*- coding: utf-8 -*-

import sys
import os
from number.canvas import Canvas


class Number():
    def run(filename, pathToOpen, nb_color):
        fileDir = os.path.dirname(os.path.realpath('__file__'))
        fileIN = fileDir + f"{pathToOpen}/{filename}"
        CANVAS = Canvas(fileIN, nb_color)
        CANVAS.generate()
        CANVAS.display_colormap()
