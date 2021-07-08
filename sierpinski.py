from PIL import Image
import random

class Sierpinski:
    def __init__(self, width) -> None:
        self.width = width
        self.image = Image.new('HSV', (width, width))
        self.corners = [(0,width), (width, width), (width/2, 0)]

    def calc_image(self, iterations):
        current_point = random.choice(self.corners)
        for _ in range(iterations):
            random_corner = random.choice(self.corners)
            new_point = int((random_corner[0] + current_point[0]) // 2) , int((random_corner[1] + current_point[1]) // 2)
            self.image.putpixel(new_point, (255,255,255))
            current_point = new_point

    def get_image(self):
        return self.image

    
sier = Sierpinski(1000)
sier.calc_image(10000)
image = sier.get_image()

image.show()

# Must convert to RGB mode in order to save as PNG
# image = image.convert('RGB')
# image.save('drawing.png', 'PNG')