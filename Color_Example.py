from Image import ImageObject
from Histogram import rgb_histogram

path = "images/"
image = ImageObject(path + "eu.png")
image.load_image()
#image.set_size(512, 512)


sample_grid = int(input("Enter an even value for sample grid: "))
while sample_grid % 2 != 0:
    sample_grid = int(input("Enter an even value for sample grid: "))

level = int(input("Enter an even value for levels of RGB: "))
while level % 2 != 0:
    level = int(input("Enter an even value for levels of RGB: "))

image.discretize(sample_grid)
image.quantize(level)

rgb_histogram(image)
image.save_image(path + f"color/color_quantize{level}_discretize{sample_grid}_cat.png")
image.show_image()