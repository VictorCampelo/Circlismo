import os
import cv2
import numpy as np

class Circlism:
    def __init__(self, filename, path_to_open, path_to_open_back, path_to_save):
        # Check if the output directory exists, if not, create it
        os.makedirs(path_to_save, exist_ok=True)

        # Paths for input, background, and output files
        self.file_in = os.path.join(path_to_open, filename)
        self.file_back = os.path.join(path_to_open_back, filename)
        self.path_to_save = os.path.join(path_to_save, filename)

        # Load input and background images
        self.image = self.load_image(self.file_in)
        self.back1 = self.file_back

        # Initialize image size and other parameters
        self.size_x, self.size_y, self.size, self.two_pi = self.initialize_params()

    def load_image(self, path):
        # Load image from the given path
        img = cv2.imread(path)

        # Check if the image is successfully loaded
        if img is None:
            print(f"Error: Unable to read image file '{path}'")
            return None

        # Convert BGR image to RGB
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        return img

    def initialize_params(self):
        # Check if the image is loaded successfully
        if self.image is None:
            return 0, 0, 0, 0

        # Calculate image size and other parameters
        size_x = self.image.shape[1]
        size_y = self.image.shape[0]
        size = min(size_x, size_y)
        two_pi = 2.0 * 3.14
        return size_x, size_y, size, two_pi

    def process_image(self):
        # Check if the image is loaded successfully
        if self.image is None:
            print("Error: Unable to load the image.")
            return None

        # Apply Canny edge detection
        canny = cv2.Canny(self.image, 200, 300)

        # Invert the edges
        edges_inv = 255 - canny

        # Calculate distance transform
        dist_transform = cv2.distanceTransform(edges_inv, cv2.DIST_L2, 0)

        return dist_transform

    def add_new_circles(self, is_filled, dist_map, circles, radius, threshold, edge_threshold):
        for x in range(2 * radius, self.size_x - radius):
            for y in range(2 * radius, self.size_y - radius):
                if dist_map[y, x] > radius:
                    circle_radius = min(int((dist_map[y, x] + 1) / 2), radius, edge_threshold)
                    if self.is_valid_circle(x, y, circle_radius, is_filled):
                        circles.append({'x': x, 'y': y, 'radius': circle_radius})
                        self.fill_circle(x, y, circle_radius, is_filled)
                        y += circle_radius * 2 + radius

    def is_valid_circle(self, x, y, radius, is_filled):
        for i in range(x - radius, x + radius + 1):
            if not (0 <= i < self.size_x):
                break
            dx = i - x
            for j in range(y - radius, y + radius + 1):
                if not (0 <= j < self.size_y):
                    break
                dy = j - y
                if dx ** 2 + dy ** 2 < (radius + 1) ** 2 and is_filled[i, j] == 1:
                    return False
        return True

    def fill_circle(self, x, y, radius, is_filled):
        for i in range(x - radius, x + radius + 1):
            if not (0 <= i < self.size_x):
                break
            dx = i - x
            for j in range(y - radius, y + radius + 1):
                if not (0 <= j < self.size_y):
                    break
                dy = j - y
                if dx ** 2 + dy ** 2 <= (radius + 1) ** 2:
                    is_filled[i, j] = 1

    def save_svg(self, circles):
        svg_header = f'<svg xmlns="http://www.w3.org/2000/svg" width="{self.size_x}" height="{self.size_y}">\n'
        svg_footer = '</svg>'
        svg_circles = ''

        for c in circles:
            x = c['x']
            y = c['y']
            radius = c['radius']
            color = self.image[y, x]  # Get color from original image
            svg_color = f'rgb({color[0]}, {color[1]}, {color[2]})'
            svg_circles += f'<circle cx="{x}" cy="{y}" r="{radius}" fill="{svg_color}" />\n'

        svg_content = svg_header + svg_circles + svg_footer

        # Change file extension to SVG
        svg_filename = os.path.splitext(self.path_to_save)[0] + '.svg'

        with open(svg_filename, 'w') as f:
            f.write(svg_content)

    def run_circlism(self):
        # Process the input image
        processed_image = self.process_image()

        # Check if the image is loaded successfully
        if processed_image is None:
            return

        # Detect circles and draw them
        circles = []
        is_fill = np.zeros([self.size_x + 1, self.size_y + 1])

        # Define the base circle radii for an image of size 1024x1024
        base_circle_radii = [150, 120, 90, 60, 30, 20, 10]

        # Calculate the maximum distance value in the distance transform
        width = processed_image.shape[1]

        # Scale the base circle radii based on the maximum distance
        circle_radii = [int(radius * width / 1024) for radius in base_circle_radii]

        for i in range(1, len(circle_radii)):
            self.add_new_circles(is_fill, processed_image, circles, circle_radii[i], circle_radii[i], circle_radii[i - 1])

        # Save circles as SVG
        self.save_svg(circles)
