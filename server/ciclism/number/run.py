# -*- coding: utf-8 -*-

import sys
import os
from canvas import Canvas

class number():
    def run(filename, pathToOpen, nb_color):
        CANVAS = Canvas(f'..{pathToOpen}/{filename}', nb_color)
        CANVAS.generate()
        CANVAS.display_colormap()
