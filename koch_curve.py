from PIL import Image, ImageDraw
import numpy as np


class KochCurve():
    def __init__(self, initial_line, depth):
        self.initial_line = initial_line#[np.array(initial_line[0]), np.array(initial_line[1])]
        self.depth = depth
        self.image = Image.new('HSV', (2000, 2000))
        
        self.draw = ImageDraw.Draw(self.image)

    def q1_curve(self, start_point, end_point):
        v = (np.array(end_point) - np.array(start_point))/3
        a = start_point
        b = tuple(start_point + v)
        c = tuple(np.array(b) + np.array([v[1], -v[0]]) )
        d = tuple(c + v)
        e = tuple(end_point - v)
        f = end_point
        end_point
        lines = [[a, b]]
        lines.append([b,c])
        lines.append([c,d])
        lines.append([d,e])
        lines.append([e,f])
        return lines

    def q2_curve(self, start_point, end_point):
        v = (np.array(end_point) - np.array(start_point))/4
        v2 = (np.array([v[1], -v[0]])) 
        a = start_point
        b = tuple(start_point + v)
        c = tuple(np.array(b) + v2)
        d = tuple(c + v)
        e = tuple(np.array(d) - 2*v2)
        f = tuple(e + v)
        g = tuple(f+v2)
        h = end_point
        end_point
        lines = [[a, b]]
        lines.append([b,c])
        lines.append([c,d])
        lines.append([d,e])
        lines.append([e,f])
        lines.append([f,g])
        lines.append([g,h])

        return lines

    def draw_segment(self, start_point, end_point, depth):
        lines = self.q2_curve(start_point, end_point)
        for line in lines:
            if depth <= 0:
                self.draw.line(line, fill=(100, 100, 200)),
            else:
                self.draw_segment(line[0], line[1], depth-1)

    def get_image(self):
        for i in range(len(self.initial_line)-1):
            self.draw_segment(self.initial_line[i], self.initial_line[i+1], self.depth)
        return self.image

curve = KochCurve(((400, 400), (1600, 400), (1600, 1600), (400, 1600), (400, 400)), 2)
curve.get_image().show()