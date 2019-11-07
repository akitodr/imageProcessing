from Image import ImageObject
import numpy as np

path = "images/"
image = ImageObject(path + "greyscale.png")
image.load_image()
image.set_size(512, 512)
image.set_image_to_gray()
image.save_image(path + "pb.png")

weighted_average = [[1.5, 2.0, 2.5], [2.0, 4.0, 2.0], [1.5, 2.0, 1.5]]
laplace = [[0.0, -1.0, 0.0], [-1.0, 4.0, -1.0], [0.0, -1.0, 0.0]]
sharpen = [[-1.0, -1.0, -1.0], [-1.0, 9.0, -1.0], [-1.0, -1.0, -1.0]]
border_detection = [[-1.0, -1.0, -1.0], [-1.0, 8.0, -1.0], [-1.0, -1.0, -1.0]]
sobel_a = np.square([[-1.0, -2.0, -1.0], [0.0, 0.0, 0.0], [1.0, 2.0, 1.0]]) #primeira matriz elevada ao quadrado
sobel_b = np.square([[-1.0, 0.0, -1.0], [-2.0, 0.0, 2.0], [-1.0, 0.0, 1.0]]) #segunda matriz elevada ao quadrado
final_sobel = np.sqrt(sobel_a + sobel_b) #resultado final é a raiz da soma das matrizes anteriores


def saturate(value):
    if value > 255:
        return 255
    if value < 0:
        return 0
    return value


for y in range(image.get_height()):
    for x in range(image.get_width()):

        for kx in range(0, 3):
            for ky in range(0, 3):
                px = x + (kx - 1)
                py = y + (ky - 1)
                if px < 0 or px >= image.get_width() or py < 0 or py >= image.get_height():
                    continue

                gray_scale = image.get_grayscale(px, py) * laplace[kx][ky]
        new_scale = saturate(gray_scale)
        image.set_pixel(x, y, int(gray_scale))


image.save_image(path + "laplace.png")
image.show_image()