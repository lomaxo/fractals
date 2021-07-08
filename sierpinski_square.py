from PIL import Image
import random

class Sierpinski:
    def __init__(self, side_length) -> None:
        # Square
        self.width = side_length
        self.height = side_length
        self.image = Image.new('HSV', (self.width+1, self.height+1))
        self.corners = [(0, self.height), (self.width, self.height), (self.width, 0), (0,0)]

    def calc_image(self, iterations):
        current_point = random.choice(self.corners)
        random_corner = last_corner = current_point
        for _ in range(iterations):
            while random_corner == last_corner:
                random_corner = random.choice(self.corners)
            last_corner = random_corner
            new_point = int((random_corner[0] + current_point[0]) // 2) , int((random_corner[1] + current_point[1]) // 2)
            self.image.putpixel(new_point, (100,255,100))
            current_point = new_point

    def get_image(self):
        return self.image

    
sier = Sierpinski(1000)
sier.calc_image(1000000)
image = sier.get_image()

image.show()

# Must convert to RGB mode in order to save as PNG
# image = image.convert('RGB')
# image.save('drawing.png', 'PNG')