# Fractals

## Drawing Pixels in Python

### Pillow
Pillow is a _fork_ of the Python Image Library allows drawing and manipulation images in Python. 
It can be installed using pip:

```
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade Pillow
```
For our purposes we need to
- create an Image object (using HSV or RGB) and
- use ```putpixel(position, colour)``` to draw a pixel onto that image. In this case:
  - position is a tuple of two values: x and y. 
  - colour is tuple of 3 values: Hue, Saturation, Value or Red, Green, Blue depending on the image type. 
- Display the image using ```show()```

```python
from PIL import Image

size = (255, 255)
image = Image.new('HSV', size)
max_x, max_y = size
for x in range(max_x):
    for y in range(max_y):
        hue = x
        saturation = y
        value = 255
        image.putpixel((x ,y), (hue, saturation, value))

image.show()
```
You can also save the image to a file. Some file formats require RGB instead of HSV.

```python
image = image.convert('RGB')
image.save('drawing.png', 'PNG')
```
If you want to draw lines instead of individual pixels you can create a draw object for the image:
```python
draw = ImageDraw.Draw(image)
draw.line([x1, y1, x2, y2])
```
See the documentation for more details: https://pillow.readthedocs.io/en/stable/reference/ImageDraw.html

### OpenCV

Pillow doesn't do video or live updating of images very well. One alternative is to use OpenCV. This uses _numpy_ arrays so there is a slightly steeper learning curve.
An image is stored as a numpy array of values. You can create an empty image like this:

- create a numpy array to hold the pixel data
- update individual pixels by setting the relevent values in the array
- set up a loop
- continually display the image using ```imshow()```
- ```imshow()``` won't create a new window each time. Instead it updates an existing window if one exists.

```python
import cv2
import numpy as np

image = np.zeros(shape=(100, 100, 3))

image[(50, 50)] = (255, 255, 255)

while True:
    cv2.imshow('image', image)
    if cv2.waitKey(1) == ord('q'):
        break
```

## Sierpinski

- The basic traingle using Chaos Game
- Explanation why it works: <https://en.wikipedia.org/wiki/Chaos_game>
- Extend to other shapes...

## Koch Curve

- <https://en.wikipedia.org/wiki/Koch_snowflake>

## Barnsley Fern

- Similar random technique for drawing it
- Using separate arrays for data and image

## Mandelbrot

- Explanation of the technique (see numberphile/computerphile video?)
- Full image (b&w)
- Add colour
- Zooming in on an area
- Julia set?

## Fractal Trees

- Basic idea
- Using recursion
