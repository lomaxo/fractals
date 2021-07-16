from PIL import Image



class Mandelbrot:
    def count_divergence(self, c, max_iterations=255):
        i = 0
        z = 0
        while i < max_iterations:
            z = z**2 + c
            if abs(z) > 2:
                return i
            i += 1
        return i

    def calculate_values(self, a_min=-2.25, a_max=.75, b_min=-1.5, b_max=1.5, max_i=255, width=1000, height=1000):
        # a_min = -2.25
        # a_max = .75
        # b_min = -1.5
        # b_max = 1.5

        # a_min = -.8
        # a_max = -.7
        # b_min = 0
        # b_max = 0.1
        image = Image.new('HSV', (width, height))
        a_range = a_max - a_min
        b_range = b_max - b_min
        # pixels = []
        a = a_min
        while a < a_max:
            b = b_min
            while b < b_max:
                x = int((a - a_min) / a_range * width)
                y = int((b - b_min) / b_range * height)
                n = self.count_divergence(complex(a, b), max_i)
                colour = (n, 200, 200) if n < max_i else (0, 100, 0)
                image.putpixel((x, y), colour)
                b += b_range / height
            a += a_range / width
        return image

def demo_image():
    mandelbrot = Mandelbrot()
    image = mandelbrot.calculate_values(width=500, height=500)
    image.show()
    image.convert('RGB').save('mandelbrot.png')


def animate():
    mandelbrot = Mandelbrot()
    x1 = -2.25
    x2 = .25
    y1 = -1.5
    y2 = 1.5

    for i in range(3):
        x1 = x1 / 2
        x2 = x2 / 2
        y1 = y1 / 2
        y2 = y2 / 2
        image = mandelbrot.calculate_values(a_min=x1, a_max=x2, b_min=y1, b_max=y2, width=500, height=500)
        image.show()

demo_image()