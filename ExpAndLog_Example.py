from Image import ImageObject
from Histogram import gray_histogram
from copy import deepcopy

path = "images/"
image = ImageObject(path + "greyscale.png")
image.load_image()
image.set_size(512, 512)
image.set_image_to_gray()
image.save_image(path + "pb.png")
exp_image = deepcopy(image)
log_image = deepcopy(image)

exp_image.exponential()
exp_image.save_image(path + "expandlog/exponential.png")
log_image.logarithm()
log_image.save_image(path + "expandlog/logarithm.png")

image.show_image()
gray_histogram(image)
exp_image.show_image()
gray_histogram(exp_image)
log_image.show_image()
gray_histogram(log_image)
