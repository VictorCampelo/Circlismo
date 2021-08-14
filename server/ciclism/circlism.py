import os
import cv2
import cairo
import time
import numpy as np


class Circlism():
    def __init__(self, filename, pathToOpen, pathToOpenBack, pathToSave):
        fileDir = os.path.dirname(os.path.realpath('file'))
        fileIN = fileDir + f"{pathToOpen}/{filename}"
        fileBACK = fileDir + f"{pathToOpenBack}/{filename}"
        fileOUT = fileDir + f"{pathToSave}/{filename}"

        self.pathToSave = fileOUT
        self.image = self.load_image(fileIN)
        self.back = self.load_image(fileBACK)
        self.back1 = fileBACK
        self.SIZE_X = self.image.shape[1]
        self.SIZE_Y = self.image.shape[0]
        self.SIZE = min(self.SIZE_X, self.SIZE_Y)
        self.TWOPI = 2.0 * 3.14

    def load_image(self, path):
        Image1 = cv2.imread(path)
        Image1 = cv2.cvtColor(Image1, cv2.COLOR_BGR2RGB)
        return Image1

    def process_image(self):
        canny = cv2.Canny(self.image, 200, 300)

        edges_inv = (255 - canny)

        dist_transform = cv2.distanceTransform(edges_inv, cv2.DIST_L2, 0)

        return dist_transform

    def add_new_circles(self, is_fill, dist_map, circles, r, t, e):
        for x in range(2 * r, self.SIZE_X - r):
            for y in range(2 * r, self.SIZE_Y - r):
                a = True
                if dist_map[y, x] > r:
                    p = (int)((dist_map[y, x] + 1) / 2)
                    if p > e:
                        p = r
                    if (is_fill[x, y]
                            == 0) & (x - p >= 0) & (x + p < self.SIZE_X) & (
                                y - p >= 0) & (y + p < self.SIZE_Y):
                        for rt in range(x - p, x + p + 1):
                            if rt > self.SIZE_X:
                                break
                            yu = rt - x
                            for ty in range(y - p, y + p + 1):
                                if ty > self.SIZE_Y:
                                    break
                                op = ty - y
                                if yu * yu + op * op < (p + 1) * (p + 1):
                                    if is_fill[rt, ty] == 1:
                                        a = False
                                        break
                                if a == False:
                                    break

                        if a == True:
                            circles.append({
                                'x': x,
                                'y': y,
                                'r': p,
                            })
                            for st in range(x - p, x + p + 1):
                                ui = st - x
                                if st > self.SIZE_X:
                                    break
                                for en in range(y - p, y + p + 1):
                                    iu = en - y
                                    if en > self.SIZE_Y:
                                        break
                                    if ui * ui + iu * iu <= (p + 1) * (p + 1):
                                        is_fill[st, en] = 1

                            y = y + p * 2 + r

    def show(self, img_clr, back, ctx, circles):
        for c in circles:
            if (not np.array_equal(back[int(c['y']), int(c['x'])],
                                   np.array([200, 200, 200]))):
                rgb = img_clr[int(c['y']), int(c['x'])]
                rgba = [rgb[0] / 255, rgb[1] / 255, rgb[2] / 255, 1.0]
                ctx.set_source_rgba(*rgba)
                ctx.arc(c['x'], c['y'], c['r'], 0, self.TWOPI)
                ctx.fill()
                ctx.set_source_rgba(*[0, 0, 0, 1])
                ctx.arc(c['x'], c['y'], c['r'], 0, self.TWOPI)
                ctx.stroke()
            else:
                rgb = img_clr[int(c['y']), int(c['x'])]
                rgba = [rgb[0] / 255, rgb[1] / 255, rgb[2] / 255, 0.7]
                ctx.set_source_rgba(*rgba)
                ctx.arc(c['x'], c['y'], c['r'], 0, self.TWOPI)
                ctx.fill()
                ctx.set_source_rgba(*[0, 0, 0, 1])

    def run_circlism(self):
        processed_image = self.process_image()
        back = cv2.imread(self.back1)
        s = time.time()
        image2 = cairo.ImageSurface.create_from_png(self.back1)
        buffer_surf = cairo.ImageSurface(cairo.FORMAT_ARGB32, self.SIZE_X,
                                         self.SIZE_Y)
        buffer = cairo.Context(buffer_surf)
        # buffer.set_source_surface(self.image, 0,0)
        # buffer.set_source_rgba(0,0,0,1)
        buffer.paint()

        # buffer.scale(self.SIZE_X, self.SIZE_Y)

        buffer.rectangle(0.0, 0.0, 1.0, 1.0)
        buffer.fill()
        circles = []
        is_fill = np.zeros([self.SIZE_X + 1, self.SIZE_Y + 1])
        # D = [300, 200]
        # D = [300, 200, 100]
        D = [200, 90, 60, 30, 20, 15]
        # D = [ 40,30 ]
        # add_new_circles(is_fill, processed_image, circles,40,40,100)
        print(time.time() - s)
        for i in range(len(D)):
            if i == 0:
                continue
            self.add_new_circles(is_fill, processed_image, circles, D[i], D[i],
                                 D[i - 1])
            print(time.time() - s)

        buffer.set_line_width(1)
        self.show(self.image, back, buffer, circles)
        print(len(circles))
        buffer_surf.write_to_png(self.pathToSave)
        print(time.time() - s)
