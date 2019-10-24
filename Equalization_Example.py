from Image import ImageObject
from Histogram import gray_histogram
from copy import deepcopy

path = "images/"
image = ImageObject(path + "greyscale.png")
image.load_image()
image.set_size(512, 512)
image.set_image_to_gray()
image.save_image(path + "pb.png")
old_image = deepcopy(image)

image.equalization()
image.save_image(path + "equalization/equalization.png")

old_image.show_image()
gray_histogram(old_image)

image.show_image()
gray_histogram(image)