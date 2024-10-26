from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load
from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey  # Replace 'your_module_name' with the actual module name

def display_image(array, title):
    """Helper function to display an image."""
    plt.imshow(array)
    plt.title(title)
    plt.axis('off')
    plt.show()

def main():
    # Load and prepare the image
    path = "../ex02/image.jpeg"  # Path to your test image
    # img = Image.open(path).convert("RGB")
    pixel_data = ft_load(path)

    # Before applying filters
    display_image(pixel_data, "Original Image")

    # Apply each filter and display the result
    inverted_img = ft_invert(pixel_data)
    display_image(inverted_img, "Inverted Image")

    red_img = ft_red(pixel_data)
    display_image(red_img, "Red Filter")

    green_img = ft_green(pixel_data)
    display_image(green_img, "Green Filter")

    blue_img = ft_blue(pixel_data)
    display_image(blue_img, "Blue Filter")

    grey_img = ft_grey(pixel_data)
    display_image(grey_img, "Grayscale Image")

    print(ft_invert.__doc__)

if __name__ == "__main__":
    main()
