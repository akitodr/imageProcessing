from Image import ImageObject
from Histogram import gray_histogram

path = "images/"
image = ImageObject(path + "cat.png")
image.load_image()
image.set_size(512, 512)
image.set_image_to_gray()
image.save_image(path + "_pb.png")

sample_grid = int(input("Enter an even value for sample grid: "))
while sample_grid % 2 != 0:
    sample_grid = int(input("Enter an even value for sample grid: "))

level = int(input("Enter an even value for levels of gray: "))
while level % 2 != 0:
    level = int(input("Enter an even value for levels of gray: "))

image.gray_discretize(sample_grid)
image.gray_quantize(level)

gray_histogram(image)
image.save_image(path + f"/gray/gray_quantize{level}_discretize{sample_grid}_cat.png")
image.show_image()