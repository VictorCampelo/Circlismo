# -*- coding: utf-8 -*-
from ciclism.meanshift import Meanshift
from number.run import Number
from ciclism.circlism import Circlism
from ciclism.backgroud import Backgroud
import cv2


class Circle():
    def __init__(self, filename):
        self.filename = filename

    def run(self):
        Meanshift(self.filename, pathToOpen='/uploads/input',
                  pathToSave='/uploads/input').seg()
        Backgroud(self.filename,
                  pathToOpen='/uploads/intermediate',
                  pathToSave='/uploads/intermediate/backgroud')
        Circlism(self.filename,
                 pathToOpen='/uploads/intermediate',
                 pathToOpenBack='/uploads/intermediate/backgroud',
                 pathToSave='/uploads/output').run_circlism()
        Number.run(self.filename, '/uploads/output', 40)
