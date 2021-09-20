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
- create an Image object (using HSV or RGB)
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

Use PIL ImageDraw to draw lines.
Create a KochCurve class:

| property | Description|
|---|---|
|initial_line | The coordinates of the line which should be recursively redrawn|
| depth | The number of recursions to draw |
| image | The PIL image object that the curve will be drawn onto |
| draw | The PIL ImageDraw object that is used to draw lines onto an image |

```python
from PIL import Image, ImageDraw
class KochCurve():
    def __init__(self, initial_line, depth):
        self.initial_line = initial_line
        self.depth = depth
        self.image = Image.new('RGB', (2000, 2000))
        self.draw = ImageDraw.Draw(self.image)
```


Create a method that returns a series of lines relative to a start and end point. This is the shape of a single segment of the Koch curve. This involves a bit of vector maths which numpy can make easier.
In this example, 
- v is a line one third the length of the full segment. 
- point c is the where the line turns 90 degrees.

```python
import numpy as np
...
    def q1_curve(self, start_point, end_point):
        v = (np.array(end_point) - np.array(start_point))/3
        a = start_point
        b = tuple(start_point + v)
        c = tuple(np.array(b) + np.array([v[1], -v[0]]) )
        d = tuple(c + v)
        e = tuple(end_point - v)
        f = end_point
        lines = [[a, b]]
        lines.append([b,c])
        lines.append([c,d])
        lines.append([d,e])
        lines.append([e,f])
        return lines
```

The recursive part of the algorithm happens here:
```python
  def draw_segment(self, start_point, end_point, depth):
        lines = self.curve_func(self, start_point, end_point)
        for line in lines:
            if depth <= 0:
                self.draw.line(line, fill=self.fill),
            else:
                self.draw_segment(line[0], line[1], depth-1)
```

If we have reached depth = 0, just draw the series of lines returned by the previous function.
If depth > 0 we want to instead draw a smaller segment where each line would go, so this function calls itself recursively, but _with a lower value for depth_.


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
