import cv2
import numpy as np
from sklearn.cluster import MeanShift, estimate_bandwidth
import os

class Meanshift():
    def __init__(self, filename, pathToOpen, pathToSave):
        fileDir = os.path.dirname(os.path.realpath('__file__'))
        self.fileIN = fileDir + f"{pathToOpen}/{filename}"
        self.fileOUT = fileDir + f"{pathToSave}/result.png"

    def seg(self):
        path = self.resize(self.fileIN)
        img = cv2.imread(path)
        img = cv2.medianBlur(img, 3)

        img_seg5 = self.shift_seg(img)
        cv2.imwrite(self.fileOUT, img_seg5)
        self.resizeTo1024(2048, self.fileOUT)

    def resize(self, path):
        img = cv2.imread(path, cv2.IMREAD_UNCHANGED)

        if(img.shape[0] <= 1024 and img.shape[1] <= 1024):
            return path
        else:
            (h, w) = img.shape[:2]
            r = 512 / float(w)
            dim = (512, int(h * r))

            # resize image
            resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

            cv2.imwrite(path, resized)
            return path
    
    def resizeTo1024(self, value, path):
        img = cv2.imread(path, cv2.IMREAD_UNCHANGED)

        (h, w) = img.shape[:2]
        r = value / float(w)
        dim = (value, int(h * r))

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
        ms = MeanShift(bandwidth, max_iter=800, bin_seeding=True)
        ms.fit(flat_image)
        labeled = ms.labels_

        segments = np.unique(labeled)

        center_feature = np.uint8(ms.cluster_centers_)
        res_feature = center_feature[labeled.flatten(), 0:3]
        res_feature = res_feature.reshape(img.shape)

        return res_feature
