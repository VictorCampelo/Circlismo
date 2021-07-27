# -*- coding: utf-8 -*-

import sys
import os
from number.canvas import Canvas


class Number():
    def __init__(self, filename, pathToOpen):
        fileDir = os.path.dirname(os.path.realpath('__file__'))
        self.fileIN = fileDir + f"{pathToOpen}/{filename}"

    def run(self, nb_color):
        CANVAS = Canvas(self.fileIN, nb_color)
        CANVAS.generate()
        CANVAS.display_colormap()
