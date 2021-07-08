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

# Must convert to RGB mode in order to save as PNG
# image = image.convert('RGB')
# image.save('drawing.png', 'PNG')