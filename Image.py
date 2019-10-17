from PIL import Image, ImageFont, ImageDraw, ImageOps

class ImageObject():

    def __init__(self, path):
        self.path = path

    def load_image(self):
        try:
            self.image = Image.open(self.path)
        except:
            print('Skipping unreadable image {}'.format(self.path))

    def show_image(self):
        self.image.show()

    def save_image(self, name):
        self.image.save(name)

    def set_size(self, width, height):
        self.image = self.image.resize((width, height), Image.ANTIALIAS)

    def set_image_to_gray(self):
        self.grayimage = ImageOps.grayscale(self.image)
        self.image = self.grayimage

    def set_pixel(self, x, y, value):
        self.image.putpixel((x, y), value)

    def get_width(self):
        return self.image.width

    def get_height(self):
        return self.image.height

    def get_rgb(self, x, y):
        return self.image.getpixel((x, y))

    def get_grayscale(self, x, y):
        try:
            return self.grayimage.getpixel((x,y))
        except:
            print("You must call set_image_to_gray method first.")

    def get_histogram(self):
        return self.image.histogram()

    def get_info(self):
        print(f"Width: {self.image.width}, Height: {self.image.height}, Mode: {self.image.mode}, Format: {self.image.format}")

    def getMin(self):
        percent = (self.get_width() * self.get_height()) * 0.1
        min = 260
        for y in range(self.get_height()):
            for x in range(self.get_width()):
                if self.get_grayscale(x, y) < min:
                    min = self.get_grayscale(x, y)
        return min

    def getMax(self):
        max = -1
        for y in range(self.get_height()):
            for x in range(self.get_width()):
                if self.get_grayscale(x, y) > max:
                    max = self.get_grayscale(x, y)
        return max

    #simple linear enhancement

    def linearSum(self, value):
        for y in range(self.get_height()):
            for x in range(self.get_width()):
                self.set_pixel(x, y, self.get_grayscale(x, y) + value)

    def linearSub(self, value):
        for y in range(self.get_height()):
            for x in range(self.get_width()):
                self.set_pixel(x, y, self.get_grayscale(x, y) + (-value))

    def linearMult(self, value):
        for y in range(self.get_height()):
            for x in range(self.get_width()):
                self.set_pixel(x, y, int(self.get_grayscale(x, y) * value))

    def linearDiv(self, value):
        for y in range(self.get_height()):
            for x in range(self.get_width()):
                self.set_pixel(x, y, int(self.get_grayscale(x, y) / value))

    ###########################

    def stretch(self):
        max = self.getMax()
        min = self.getMin()
        print(max, min)
        gain = 255 / (max - min)
        for y in range(self.get_height()):
            for x in range(self.get_width()):
                result = int((self.get_grayscale(x, y) - min) * gain)
                self.set_pixel(x, y, result)

    def quantize(self, level):
        color = 255 // (level - 1)
        for y in range(self.get_height()):
            for x in range(self.get_width()):
                r, g, b, _ = self.get_rgb(x, y)
                new_r = round(r / color) * color
                new_g = round(g / color) * color
                new_b = round(b / color) * color
                self.set_pixel(x, y, (new_r, new_g, new_b))

    def discretize(self, sample_grid):
        size_width = self.get_width() // sample_grid
        size_height = self.get_height() // sample_grid
        for row in range(sample_grid):
            for col in range(sample_grid):
                r_sum = 0
                g_sum = 0
                b_sum = 0
                for y in range(size_height):
                    for x in range(size_width):
                        px = x + col * size_width
                        py = y + row * size_height
                        r, g, b, _ = self.get_rgb(px, py)
                        r_sum += r
                        g_sum += g
                        b_sum += b
                average_r = r_sum // (size_width * size_height)
                average_g = g_sum // (size_width * size_height)
                average_b = b_sum // (size_width * size_height)
                for y in range(size_height):
                    for x in range(size_width):
                        px = x + col * size_width
                        py = y + row * size_height
                        self.set_pixel(px, py, (average_r, average_g, average_b))

    def gray_quantize(self, gray_level):
        gray_foo = 255 // (gray_level - 1)

        for y in range(self.get_height()):
            for x in range(self.get_width()):
                pixel_scale = self.get_grayscale(x, y)
                new_scale = round(pixel_scale / gray_foo) * gray_foo
                self.set_pixel(x, y, new_scale)

    def gray_discretize(self, sample_grid):
        size_width = self.get_width() // sample_grid
        size_height = self.get_height() // sample_grid

        for row in range(sample_grid):
            for col in range(sample_grid):
                pixelsum = 0
                for y in range(size_height):
                    for x in range(size_width):
                        px = x + col * size_width
                        py = y + row * size_height
                        pixelsum += self.get_grayscale(px, py)
                average = pixelsum // (size_width * size_height)
                for y in range(size_height):
                    for x in range(size_width):
                        px = x + col * size_width
                        py = y + row * size_height
                        self.set_pixel(px, py, average)