import cv2
import numpy as np
import os

class Backgroud:
    def __init__(self, filename, pathToOpen, pathToSave):
        # Construct full paths for input and output files
        input_file = os.path.join(pathToOpen, filename)
        output_file = os.path.join(pathToSave, filename)

        # Check if the output directory exists, if not, create it
        os.makedirs(pathToSave, exist_ok=True)

        # Check if the input file exists
        if not os.path.exists(input_file):
            print(f"Error: Input file '{input_file}' not found.")
            return

        # Load the input image
        img = cv2.imread(input_file)

        # Check if the image is successfully loaded
        if img is None:
            print(f"Error: Unable to read image file '{input_file}'.")
            return

        # # Remove noise using Gaussian blur
        # blurred = cv2.GaussianBlur(img, (5, 5), 0)

        # # Detect edges in the image
        # edgeImg = self.edgedetect(blurred)

        # # Find significant contours
        # significant_contours = self.find_significant_contours(edgeImg)

        # # Draw significant contours on the input image
        # cv2.drawContours(img, significant_contours, -1, (0, 255, 0), 2)

        # Write the processed image to the output file
        cv2.imwrite(output_file, img)

    def edgedetect(self, img):
        # Convert the image to grayscale
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        # Apply Sobel edge detection
        sobelX = cv2.Sobel(gray_img, cv2.CV_16S, 1, 0)
        sobelY = cv2.Sobel(gray_img, cv2.CV_16S, 0, 1)
        sobel = np.hypot(sobelX, sobelY)

        # Normalize the edge image
        sobel /= sobel.max() / 255
        return sobel.astype(np.uint8)

    def find_significant_contours(self, edgeImg):
        contours, _ = cv2.findContours(edgeImg, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        significant = [cnt for cnt in contours if cv2.contourArea(cnt) > 0.05 * edgeImg.size]
        return significant
