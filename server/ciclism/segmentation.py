import cv2
import pymeanshift as pms
import os


class Segmentation():
    def operate(filename):

        fileDir = os.path.dirname(os.path.realpath('__file__'))
        fileIn = os.path.join(fileDir, f'../uploads/input/{filename}.png')

        original_image = cv2.imread(fileIn)

        (segmented_image, labels_image,
         number_regions) = pms.segment(original_image,
                                       spatial_radius=9,
                                       range_radius=3,
                                       min_density=20)

        fileIntermediate = os.path.join(
            fileDir, f'../uploads/intermediate/{filename}.png')
        cv2.imwrite(fileIntermediate, segmented_image)
