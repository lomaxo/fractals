import cv2
import numpy as np

image = np.zeros(shape=(100, 100, 3))

image[(50, 50)] = (255, 255, 255)

while True:
    cv2.imshow('image', image)
    if cv2.waitKey(1) == ord('q'):
        break