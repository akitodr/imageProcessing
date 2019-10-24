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

print ("""What operation do you want to perform?
    1.Sum
    2.Subtraction
    3.Multiplication
    4.Division""")
option = 0
while not int(option) in range(1,5):
    option = int(input(""))
highlight = float(input("Enter a highlight value: "))

if option == 1:
    image.linearSum(highlight)
    name = "linears/sum_h"
    image.save_image(path + name + f"{int(highlight)}.png")
if option == 2:
    image.linearSub(highlight)
    name = "linears/sub_h"
    image.save_image(path + name + f"{int(highlight)}.png")
if option == 3:
    image.linearMult(highlight)
    name = "linears/mult_h"
    image.save_image(path + name + f"{int(highlight)}.png")
if option == 4:
    image.linearDiv(highlight)
    name = "linears/div_h"
    image.save_image(path + name + f"{int(highlight)}.png")

old_image.show_image()
gray_histogram(old_image)

image.show_image()
gray_histogram(image)