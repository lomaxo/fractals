from PIL import Image, ImageDraw
import numpy as np
import random

class FractalTree():
    def __init__(self, initial_line, scale_factor, angle, depth):
        self.angle = angle
        self.initial_line = [np.array(initial_line[0]), np.array(initial_line[1])]
        self.scale_factor = scale_factor
        self.depth = depth
        self.branches = [initial_line]

    def gen_branches(self, prev_point, current_point, scaling, angle):
        next_points = []
        v = (current_point - prev_point) * scaling
        # angle += (random.random()-0.5)*np.pi/8
        rotation1 = np.array([[np.cos(angle), -np.sin(angle)],[np.sin(angle), np.cos(angle)]])
        rotation2 = np.array([[np.cos(-angle), -np.sin(-angle)],[np.sin(-angle), np.cos(-angle)]])
        # next_points.append((current_point, current_point+v))
        next_points.append((current_point, current_point+rotation1.dot(v)))
        next_points.append((current_point, current_point+rotation2.dot(v)))
        # next_points.append(random.choice([(current_point, current_point+rotation1.dot(v)), (current_point, current_point+rotation2.dot(v))]))
        return next_points

    def extend_branch(self, initial_line, depth, scaling, angle):
        if depth == 0:
            return

        new_branches = self.gen_branches(initial_line[0], initial_line[1], scaling, angle)
        self.branches += new_branches
        for branch in new_branches:
            self.extend_branch(branch, depth - 1, scaling, angle)


    def get_image(self):
        image = Image.new('HSV', (2000, 2000))
        image.putpixel((100, 100), (255, 255,255))
        draw = ImageDraw.Draw(image)
        # pixels = image.load()
        self.extend_branch(self.initial_line, self.depth, self.scale_factor, self.angle)
        for i, p in enumerate(self.branches):
            a = list(map(int, p[0]))
            b = list(map(int, p[1]))
            # h, s, v = pixels[tuple(b)]
            # print(a,b)
            draw.line(a + b, fill=(100, 100, 200), width=10)
        return image


tree = FractalTree(((1000, 2000), (1000, 1600)), 0.75, np.pi/7, 7)
image = tree.get_image()
image.show()
image = image.convert('RGB')
image.save('images/fractal_tree_example.png', 'PNG')