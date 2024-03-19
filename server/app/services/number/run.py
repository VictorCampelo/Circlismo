# -*- coding: utf-8 -*-
import os
from app.services.number.canvas import Canvas
from cairosvg import svg2png

class Number():
    def __init__(self, filename, path_to_open):
        os.makedirs(path_to_open, exist_ok=True)
        self.convert_svg_to_png(
            os.path.join(os.getcwd(), path_to_open, filename))
        self.filename = filename + '.png'
        self.fileIN = os.path.join(os.getcwd(), path_to_open, self.filename)

    def run(self, nb_color):
        CANVAS = Canvas(self.fileIN, self.filename, nb_color)
        CANVAS.generate()
        CANVAS.display_colormap()
        
    def convert_svg_to_png(self, filename):
        """Convert SVG to PNG."""
        svgPath = filename + ".svg"
        pngPath = filename + ".png"
        svg2png(url=svgPath, write_to=pngPath, scale=8, dpi=400)
        print(f"SVG converted to PNG: {pngPath}")
