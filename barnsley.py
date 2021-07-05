from PIL import Image, ImageDraw
import random
class Barnsley:
    def __init__(self, iterations, height):
        self.iterations = iterations
        self.scaling = height / 10
        self.width = int(height / 2)
        self.height = int(height)

    def f1(self, x0, y0):
        return 0.0, 0.16*y0

    def f2(self, x0, y0):
        x = 0.85*x0 + 0.04*y0
        # y = -0.04*x0 + 0.85*y0 + 1.6
        y = -0.04*x0 + 0.85*y0 + 1.6
        return x, y

    def f3(self, x0, y0):
        x = -0.15*x0 + 0.28*y0
        y = 0.26*x0 + 0.24*y0 + 1.6
        return x, y

    def f4(self, x0, y0):
        x = 0.2*x0 - 0.26*y0
        y = 0.23*x0 + 0.2*y0 + 0.44
        return x, y

    def scale_to_range(self, x, old_min, old_max, new_min, new_max):
        old_range = old_max - old_min
        new_range = new_max - new_min
        return ((x - old_min) * new_range / old_range) + new_min

    def calc_points(self, x=0, y=0):
        x_values = []
        y_values = []

        for i in range(0, self.iterations):
            p = random.randint(0, 100)
            if p < 3:
                x, y = self.f1(x, y)
            elif p < 76:
                x, y = self.f2(x, y)
            elif p < 89:
                x, y = self.f3(x, y)
            else:
                x, y = self.f4(x, y)
            plot_x = int(x * self.scaling)
            plot_y = int(y * self.scaling)
            x_values.append(plot_x)
            y_values.append(plot_y)

        # scale and fit the values...
        print(min(x_values), max(x_values), min(y_values), max(y_values))
        min_x = min(x_values)
        x_values = list(map(lambda x: x-min_x, x_values))
        print(min(x_values), max(x_values), min(y_values), max(y_values))
        # min_x = min(x_values)
        # max_x = max(x_values)
        # min_y = min(y_values)
        # max_y = max(y_values)
        # x_values = list(map(lambda x: int(self.scale_to_range(x, min_x, max_x, 0, self.width)), x_values))
        # y_values = list(map(lambda y: int(self.scale_to_range(y, min_y, max_y, 0, self.height)), y_values))
        # print(min(x_values), max(x_values), min(y_values), max(y_values))
        return x_values, y_values

    def get_image(self):
        x_values, y_values = self.calc_points()
        image = Image.new('HSV', (self.width, self.height))
        for i in range(len(x_values)):
            image.putpixel((x_values[i], y_values[i]), (100, 255, 255))
        return image

barnsley = Barnsley(500000, 1000)
x_values, y_values = barnsley.calc_points()
image = barnsley.get_image()

image.show()
image = image.convert('RGB')
image.save('barnsley_fern.png', 'PNG')
