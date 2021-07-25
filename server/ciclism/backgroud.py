import cv2
import numpy as np
import os


class Backgroud():
    def __init__(
        self,
        filename,
        pathToOpen,
        pathToSave,
    ):
        fileDir = os.path.dirname(os.path.realpath('__file__'))
        fileIN = fileDir + f"{pathToOpen}/{filename}"
        fileOUT = fileDir + f"{pathToSave}/{filename}"

        img = cv2.imread(fileIN)

        blurred = cv2.GaussianBlur(img, (5, 5), 0)  # Remove noise

        edgeImg = np.max([
            self.edgedetect(blurred[:, :, 0]),
            self.edgedetect(blurred[:, :, 1]),
            self.edgedetect(blurred[:, :, 2])
        ],
                         axis=0)

        mean = np.mean(edgeImg)
        # Zero any value that is less than mean. This reduces a lot of noise.
        edgeImg[edgeImg <= mean] = 0
        # '/content/drive/MyDrive/Colab/ciclism/images/intermediate/background/'
        cv2.imwrite(fileOUT, img)

    def edgedetect(self, channel):
        sobelX = cv2.Sobel(channel, cv2.CV_16S, 1, 0)
        sobelY = cv2.Sobel(channel, cv2.CV_16S, 0, 1)
        sobel = np.hypot(sobelX, sobelY)

        sobel[sobel > 255] = 255
        return sobel

    def findSignificantContours(img, edgeImg):
        contours, heirarchy = cv2.findContours(edgeImg, cv2.RETR_TREE,
                                               cv2.CHAIN_APPROX_SIMPLE)

        # Find level 1 contours
        level1 = []
        for i, tupl in enumerate(heirarchy[0]):
            # Each array is in format (Next, Prev, First child, Parent)
            # Filter the ones without parent
            if tupl[3] == -1:
                tupl = np.insert(tupl, 0, [i])
                level1.append(tupl)
        significant = []
        tooSmall = edgeImg.size * 5 / 100  # If contour isn't covering 5% of total area of image then it probably is too small
        for tupl in level1:
            contour = contours[tupl[0]]
            area = cv2.contourArea(contour)
            if area > tooSmall:
                significant.append([contour, area])

        significant.sort(key=lambda x: x[1])
        #print ([x[1] for x in significant]);
        return [x[0] for x in significant]
