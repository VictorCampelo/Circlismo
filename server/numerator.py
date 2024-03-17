# -*- coding: utf-8 -*-
from number.run import Number
import os

class Numerator():
    def __init__(self, filename):
        self.filename = filename

    def run(self):        
        input_dir = os.path.join('uploads', 'output')
        Number(self.filename, path_to_open=input_dir).run(40)
