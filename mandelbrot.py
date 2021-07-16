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
        """
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
        """
        for x in range(width):
            for y in range(height):
                a = (x/width) * a_range + a_min
                b = (y/height) * b_range + b_min
                n = self.count_divergence(complex(a, b), max_i)
                colour = (n, 200, 200) if n < max_i else (0, 100, 0)
                image.putpixel((x, y), colour)
        return image



def demo_image():
    mandelbrot = Mandelbrot()
    image = mandelbrot.calculate_values(width=500, height=500)
    image.show()
    image.convert('RGB').save('mandelbrot.png')


def animate(focus_x, focus_y, zoom_rate, frames):
    mandelbrot = Mandelbrot()
    x1 = -2.25
    x2 = .25
    y1 = -1.5
    y2 = 1.5
    images = []
    print("Generating frames:")
    for i in range(frames):
        image = mandelbrot.calculate_values(a_min=x1, a_max=x2, b_min=y1, b_max=y2, max_i=105, width=100, height=100)
        #image.show()
        #image.convert('RGB')
        images.append(image)
        x1 = ((x1 - focus_x) / zoom_rate) + focus_x
        x2 = ((x2 - focus_x) / zoom_rate) + focus_x
        y1 = ((y1 - focus_y) / zoom_rate) + focus_y
        y2 = ((y2 - focus_y) / zoom_rate) + focus_y
        pc_complete = (i+1)/frames*100
        if int(pc_complete) % 10 == 0:
            print(f'\n{pc_complete:.0f}%', flush=True, end='')
        else:
            print('.', end='', flush=True)
    images[0].save('out.gif', save_all=True, append_images=images[1:], loop=0)
    print('\nDone.')
animate(-1.5, 0, 1.5, 100)
#demo_image()