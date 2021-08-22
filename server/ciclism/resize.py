import cv2
import os


class Resize():
    def operate(value, filename, pathToOpen, pathToSave):
        fileDir = os.path.dirname(os.path.realpath('__file__'))
        file = os.path.join(fileDir, f'..{pathToOpen}/{filename}.jpg')
        img = cv2.imread(file, cv2.IMREAD_UNCHANGED)

        scale_percent = value  # percent of original size
        width = int(img.shape[1] * scale_percent / 100)
        height = int(img.shape[0] * scale_percent / 100)
        dim = (width, height)

        # resize image
        resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

        file = os.path.join(fileDir, f'..{pathToSave}/{filename}.png')
        cv2.imwrite(file, resized)