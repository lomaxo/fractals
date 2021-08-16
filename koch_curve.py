from PIL import Image, ImageDraw
import numpy as np


class KochCurve():
    def __init__(self, initial_line, depth):
        self.initial_line = initial_line#[np.array(initial_line[0]), np.array(initial_line[1])]
        self.depth = depth
        self.image = Image.new('HSV', (2000, 2000))
        
        self.draw = ImageDraw.Draw(self.image)

    def draw_segment(self, start_point, end_point, depth):
        v = np.array(end_point) - np.array(start_point)
        #print(start_point)
        #print(list(v + start_point))   
        a = start_point
        b = tuple(start_point + v/3)
        c = tuple(np.array(b) + np.array([(v/3)[1], (-v/3)[0]]) )
        d = tuple(c + v/3)
        e = tuple(end_point - v/3)
        f = end_point
        end_point
        lines = [[a, b]]
        lines.append([b,c])
        lines.append([c,d])
        lines.append([d,e])
        lines.append([e,f])
        for line in lines:
            #print(line)
            if depth <= 0:
                self.draw.line(line, fill=(100, 100, 200)),
            else:
                self.draw_segment(line[0], line[1], depth-1)
        #self.draw.line((start_point, end_point), fill=(100, 100, 200)) 

    def get_image(self):
        #print(self.initial_line)   
        self.draw_segment(self.initial_line[0], self.initial_line[1], self.depth)
        #self.draw.line(self.initial_line, fill=(100, 100, 200)) 
        return self.image

curve = KochCurve(((100, 1000), (1800, 1000)), 5)
curve.get_image().show()