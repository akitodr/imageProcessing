import matplotlib.pylab as plt


def rgb_histogram(image):
    pixel_list = image.get_histogram()
    plt.bar(range(256), pixel_list[:256], color='r', alpha = 0.5)
    plt.bar(range(256), pixel_list[256:2*256], color='g', alpha = 0.4)
    plt.bar(range(256), pixel_list[2*256:3*256], color='b', alpha = 0.3)
    plt.show()


def gray_histogram(image, color):
    pixel_list = image.get_histogram()
    plt.bar(range(256), pixel_list[:256], color=color, alpha = 0.5)
