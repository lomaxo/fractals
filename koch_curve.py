from PIL import Image, ImageDraw
import numpy as np


class KochCurve():
    def __init__(self, initial_line, depth, fill = (200, 200, 200)):
        self.initial_line = initial_line#[np.array(initial_line[0]), np.array(initial_line[1])]
        self.depth = depth
        self.image = Image.new('RGB', (2000, 2000))
        self.fill = fill
        self.draw = ImageDraw.Draw(self.image)

    def snowflake_curve(self, start_point, end_point):
        v = (np.array(end_point) - np.array(start_point))/3
        a = start_point
        b = tuple(start_point + v)
        c = tuple(np.array(b) + np.array([v[1], -v[0]]) + v/2 )
        d = tuple(end_point - v)
        e = end_point
        lines = [[a, b]]
        lines.append([b,c])
        lines.append([c,d])
        lines.append([d,e])
        return lines


    def q1_curve(self, start_point, end_point):
        v = (np.array(end_point) - np.array(start_point))/3
        a = start_point
        b = tuple(start_point + v)
        c = tuple(np.array(b) + np.array([v[1], -v[0]]) )
        d = tuple(c + v)
        e = tuple(end_point - v)
        f = end_point
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
        e = tuple(np.array(d) - v2)
        f = tuple(np.array(e) - v2)
        g = tuple(f + v)
        h = tuple(g+v2)
        i = end_point
        lines = [[a, b]]
        lines.append([b,c])
        lines.append([c,d])
        lines.append([d,e])
        lines.append([e,f])
        lines.append([f,g])
        lines.append([g,h])
        lines.append([h,i])
        return lines

    def draw_segment(self, start_point, end_point, depth):
        lines = self.snowflake_curve(start_point, end_point)
        for line in lines:
            if depth <= 0:
                self.draw.line(line, fill=self.fill),
            else:
                self.draw_segment(line[0], line[1], depth-1)

    def get_image(self):
        for i in range(len(self.initial_line)-1):
            self.draw_segment(self.initial_line[i], self.initial_line[i+1], self.depth)
        return self.image

# curve = KochCurve(((400, 400), (1600, 400), (1600, 1600), (400, 1600), (400, 400)), 0)
curve = KochCurve(((400, 1600), (1000, 400), (1600, 1600), (400, 1600)), 3)
curve.get_image().show()