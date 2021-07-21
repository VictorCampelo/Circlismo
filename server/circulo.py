# -*- coding: utf-8 -*-
from server.ciclism.circlism import circlism
from server.ciclism.backgroud import Backgroud
from server.ciclism.segmentation import Segmentation
from server.ciclism.resize import Resize
import cv2

filename = 'pp'


class Circle():
    def __init__(self, filename):
        self.filename = filename

    def run(self):
        Resize.operate(60,
                       self.filename,
                       pathToOpen='/uploads/input',
                       pathToSave='/uploads/input')
        Segmentation.operate(self.filename)
        Resize.operate(500,
                       self.filename,
                       pathToOpen='/uploads/intermediate',
                       pathToSave='/uploads/intermediate')
        Backgroud(self.filename,
                  pathToOpen='/uploads/intermediate',
                  pathToSave='/uploads/intermediate/backgroud')
        circlism(self.filename,
                 pathToOpen='/uploads/intermediate',
                 pathToOpenBack='/uploads/intermediate/backgroud',
                 pathToSave='/uploads/output').run_circlism()


# result = cv2.imread(f'/uploads/output/{filename}.png')
# result = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)
"""# Number"""

# cd /content/drive/MyDrive/Colab/ciclism/number

# !python run.py /content/drive/MyDrive/Colab/ciclism/images/output/pp.png 40