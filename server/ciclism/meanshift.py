import cv2
import numpy as np
from sklearn.cluster import MeanShift, estimate_bandwidth
import matplotlib.pyplot as plt
import os


class Meanshift():
    def __init__(self, filename, pathToOpen, pathToSave):
        fileDir = os.path.dirname(os.path.realpath('__file__'))
        self.fileIN = fileDir + f"{pathToOpen}/{filename}"
        self.fileOUT = fileDir + f"{pathToSave}/result.png"

    def seg(self):
        print(self.fileIN)
        print(self.fileOUT)
        path = self.resize(60, self.fileIN)
        img = cv2.imread(path)
        img = cv2.medianBlur(img, 3)

        img_seg5 = self.shift_seg(img)
        cv2.imwrite(self.fileOUT, img_seg5)
        self.resize(400, self.fileOUT)

    def resize(self, value, path):
        img = cv2.imread(path, cv2.IMREAD_UNCHANGED)

        scale_percent = value  # percent of original size
        width = int(img.shape[1] * scale_percent / 100)
        height = int(img.shape[0] * scale_percent / 100)
        dim = (width, height)

        # resize image
        resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

        cv2.imwrite(path, resized)
        return path

    def shift_seg(self, img):
        size = img.shape
        height = size[0]
        width = size[1]
        channel = size[2]

        flat_image = img.reshape((-1, 3))
        flat_image = np.float32(flat_image)

        # bandwidth = 15
        bandwidth = estimate_bandwidth(flat_image,
                                       quantile=.04,
                                       n_samples=1000)
        print("Size of bandwidth: " + str(bandwidth))
        ms = MeanShift(bandwidth, max_iter=800, bin_seeding=True)
        ms.fit(flat_image)
        labeled = ms.labels_

        segments = np.unique(labeled)
        print('Number of segments: ', segments.shape[0])

        center_feature = np.uint8(ms.cluster_centers_)
        res_feature = center_feature[labeled.flatten(), 0:3]
        res_feature = res_feature.reshape(img.shape)

        return res_feature
