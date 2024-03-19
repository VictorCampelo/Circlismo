import cv2
import numpy as np
from sklearn.cluster import MeanShift, estimate_bandwidth
import os

class Meanshift:
    def __init__(self, filename, input_path, output_path):
        self.input_file = os.path.join(input_path, filename)
        self.output_file = os.path.join(output_path, filename)

    def segment_image(self):
        output_dir = os.path.dirname(self.output_file)
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        if not os.path.exists(self.input_file):
            print(f"Error: Input image file '{self.input_file}' not found.")
            return
        
        print(f"Input file path: {self.input_file}")
        print(f"Output file path: {self.output_file}")

        image = cv2.imread(self.input_file)
        if image is None:
            print(f"Error: Unable to read image file '{self.input_file}'")
            return

        image = self.preprocess_image(image)

        segmented_image = self.apply_mean_shift_segmentation(image)
        
        cv2.imwrite(self.output_file, segmented_image)

    def resize_image(self, image, max_dimension):
        height, width = image.shape[:2]
        if height <= max_dimension and width <= max_dimension:
            return image

        ratio = max_dimension / max(height, width)
        dimensions = (int(width * ratio), int(height * ratio))
        resized_image = cv2.resize(image, dimensions, interpolation=cv2.INTER_AREA)
        return resized_image
    
    def preprocess_image(self, image):
        # Resize image if it exceeds maximum dimension
        image = self.resize_image(image, max_dimension=512)
        
        # # Apply histogram equalization to each channel
        # equalized_channels = [cv2.equalizeHist(channel) for channel in cv2.split(image)]
        # equalized_image = cv2.merge(equalized_channels)

        # Apply median blur to reduce noise
        blurred_image = cv2.GaussianBlur(src=image, ksize=(3, 3), sigmaX=2)

        return blurred_image

    def apply_mean_shift_segmentation(self, image):
        flat_image = image.reshape((-1, 3)).astype(np.float32)

        bandwidth = estimate_bandwidth(flat_image, quantile=0.04, n_samples=1000, n_jobs=-1)
        ms = MeanShift(bandwidth=bandwidth, bin_seeding=True)
        ms.fit(flat_image)
        labeled = ms.labels_

        center_colors = np.uint8(ms.cluster_centers_)
        segmented_image = center_colors[labeled.flatten()]
        segmented_image = segmented_image.reshape(image.shape)

        return segmented_image
