from Image import ImageObject
from Histogram import gray_histogram

path = "images/"
image = ImageObject(path + "_pb1.png")
image.load_image()
image.set_size(512, 512)
image.set_image_to_gray()
image.save_image(path + "_pb2.png")


gray_histogram(image)
image.show_image()

image.stretch()
image.show_image()

gray_histogram(image)