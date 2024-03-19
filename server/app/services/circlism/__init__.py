# -*- coding: utf-8 -*-

import os

from app.services.circlism.meanshift import Meanshift
from app.services.circlism.backgroud import Backgroud
from app.services.circlism.circlism import Circlism

class Circle():
    def __init__(self, filename):
        self.filename = filename

    def run(self):
        input_dir = os.path.join('uploads', 'input')
        intermediate_dir = os.path.join('uploads', 'intermediate')
        backgroud_dir = os.path.join(intermediate_dir, 'backgroud')
        output_dir = os.path.join('uploads', 'output')
        
        print("meanshift")
        Meanshift(self.filename,
                  input_path=input_dir,
                  output_path=intermediate_dir).segment_image()
        
        print("backgroud")
        Backgroud(self.filename,
                  pathToOpen=intermediate_dir,
                  pathToSave=backgroud_dir)
        
        print("ciclism")
        Circlism(self.filename,
                 path_to_open=intermediate_dir,
                 path_to_open_back=backgroud_dir,
                 path_to_save=output_dir).run_circlism()