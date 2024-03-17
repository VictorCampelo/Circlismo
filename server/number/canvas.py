# -*- coding: utf-8 -*-
"""Script to generate a canvas out of a picture"""

import os
import cv2
import numpy as np
from sklearn.cluster import KMeans
from sklearn.utils import shuffle

class Canvas:
    def __init__(self, path_pic, filename_canvas, nb_color, plot=False, save=True, pixel_size=1024):
        # Check if the image file exists
        if not os.path.exists(path_pic):
            print(f"Error: File '{path_pic}' not found.")
            return
        
        self.outputDir = os.path.join('uploads', 'output', 'number')
        os.makedirs(self.outputDir, exist_ok=True)

        self.path_pic = path_pic
        self.filename_canvas = filename_canvas
        self.filename_quantified = "edited-" + filename_canvas
        self.filename_colormap = "colormap-" + filename_canvas
        
        print(path_pic)

        self.src = cv2.cvtColor(cv2.imread(path_pic), cv2.COLOR_BGR2RGB)
        
        # Check if the image is successfully loaded
        if self.src is None:
            print(f"Error: Unable to read image file '{path_pic}'")
            return
        
        self.nb_color = nb_color
        self.plot = plot
        self.save = save
        self.pixel_size = pixel_size
        self.colormap = []
        
    def generate(self):
        """Main function"""
        im_source = self.resize()
        clean_img = self.cleaning(im_source)
        width, height, depth = clean_img.shape
        clean_img = np.array(clean_img, dtype="uint8") / 255
        quantified_image, colors = self.quantification(clean_img)
        canvas = np.ones(quantified_image.shape[:3], dtype="uint8") * 255

        for ind, color in enumerate(colors):
            self.colormap.append([int(c * 255) for c in color])
            mask = cv2.inRange(quantified_image, color, color)
            cnts = cv2.findContours(mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
            cnts = cnts[0] if len(cnts) == 2 else cnts[1]

            for contour in cnts:
                _, _, width_ctr, height_ctr = cv2.boundingRect(contour)
                if width_ctr > 1 and height_ctr > 1 and cv2.contourArea(
                        contour, True) < -5:
                    cv2.drawContours(canvas, [contour], -1, 0, 1)
                    #Add label
                    M = cv2.moments(contour)
                    if M["m00"] != 0:
                        cX = int(M["m10"] / M["m00"])
                        cY = int(M["m01"] / M["m00"])
                        cv2.putText(canvas, '{:d}'.format(ind + 1), (cX, cY), cv2.FONT_HERSHEY_SIMPLEX, 0.2, 0.25, 1)


        if self.save:
            cv2.imwrite(os.path.join(self.outputDir, self.filename_quantified),
                        cv2.cvtColor(quantified_image.astype('float32') * 255, cv2.COLOR_BGR2RGB))
            cv2.imwrite(os.path.join(self.outputDir, self.filename_canvas), canvas)
        return canvas
    
    def resize_image(self, image, max_dimension):
        height, width = image.shape[:2]
        if height <= max_dimension and width <= max_dimension:
            return image

        ratio = max_dimension / max(height, width)
        dimensions = (int(width * ratio), int(height * ratio))
        resized_image = cv2.resize(image, dimensions, interpolation=cv2.INTER_AREA)
        return resized_image

    def resize(self):
        """Resize the image to match the target width and respect the picture ratio"""
        (height, width) = self.src.shape[:2]

        if height > width:
            ratio = self.pixel_size / height
            dim = (int(width * ratio), self.pixel_size)
        else:
            ratio = self.pixel_size / width
            dim = (self.pixel_size, int(height * ratio))

        return cv2.resize(self.src, dim, interpolation=cv2.INTER_AREA)

    def cleaning(self, picture):
        """Reduction of noize, Morphomat operations, opening then closing """
        clean_pic = cv2.fastNlMeansDenoisingColored(picture, None, 20, 0, 2, 10)
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (1, 1))
        clean_pic = cv2.morphologyEx(clean_pic, cv2.MORPH_OPEN, kernel, cv2.BORDER_REPLICATE)
        clean_pic = cv2.morphologyEx( clean_pic, cv2.MORPH_CLOSE, kernel, cv2.BORDER_REPLICATE)
        return clean_pic

    def quantification(self, picture):
        """Returns the K-mean image"""
        width, height, dimension = tuple(picture.shape)
        image_array = np.reshape(picture, (width * height, dimension))
        image_array_sample = shuffle(image_array, random_state=0)[:1000]
        kmeans = KMeans(n_clusters=self.nb_color,
                        random_state=42).fit(image_array_sample)
        labels = kmeans.predict(image_array)
        new_img = self.recreate_image(kmeans.cluster_centers_, labels, width,
                                      height)
        return new_img, kmeans.cluster_centers_

    def recreate_image(self, codebook, labels, width, height):
        """Create the image from a list of colors, labels and image size"""
        vfunc = lambda x: codebook[labels[x]]
        out = vfunc(np.arange(width * height))
        return np.resize(out, (width, height, codebook.shape[1]))

    def display_colormap(self):
        """Plot or save the colormap as a picture for the user"""

        picture = np.ones(
            (len(self.colormap) * 30 + 20, 300, 3), dtype="uint8") * 255
        for ind, col in enumerate(self.colormap):
            cv2.putText(picture, '{:d}'.format(ind + 1), (10, 30 * ind + 23),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.3, 0, 2)
            cv2.rectangle(picture, (45, 30 * ind + 5), (85, 30 * ind + 25),
                          col,
                          thickness=-1)
            cv2.putText(picture, str(col), (100, 30 * ind + 23),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, 0, 2)

        if self.save:
            cv2.imwrite(os.path.join(self.outputDir, self.filename_colormap), cv2.cvtColor(picture, cv2.COLOR_BGR2RGB))
