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
        print("meanshift")
        Meanshift(self.filename,
                  pathToOpen='/uploads/input',
                  pathToSave='/uploads/intermediate').seg()
        print("backgroud")
        Backgroud("result.png",
                  pathToOpen='/uploads/intermediate',
                  pathToSave='/uploads/intermediate/backgroud')
        print("ciclism")
        Circlism("result.png",
                 pathToOpen='/uploads/intermediate',
                 pathToOpenBack='/uploads/intermediate/backgroud',
                 pathToSave='/uploads/output').run_circlism()
        Number("result.png", pathToOpen='/uploads/output').run(40)
