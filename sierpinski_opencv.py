import numpy as np
import cv2

import random

class Sierpinski:
    def __init__(self, side_length) -> None:
        # Triangle
        self.width = side_length
        self.height = int(side_length*3**0.5//2)
        self.corners = [(0, self.height), (self.width, self.height), (self.width/2, 0)]
        
        self.current_point = random.choice(self.corners)
        self.grid = np.zeros(shape=(self.width+1,self.height+1, 3))

    def calc_next_point(self):
        random_corner = random.choice(self.corners)
        new_point = int((random_corner[0] + self.current_point[0]) // 2) , int((random_corner[1] + self.current_point[1]) // 2)
        self.grid[new_point] = (255, 255, 255)
        self.current_point = new_point

    def get_image(self):
        return self.image

sier = Sierpinski(1000)

while True:    
    # Get a numpy array to display from the simulation
    npimage=sier.grid
    for _ in range(1000):
        sier.calc_next_point()
    cv2.imshow('image',npimage)
    if cv2.waitKey(1) == ord('q'):
        break
