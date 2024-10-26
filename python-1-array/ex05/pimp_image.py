import numpy as np

def ft_invert(array: np.array) -> np.array:
    """Inverts the color of the image received."""
    return 255 - array  # Using =, -, and +

def ft_red(array: np.array) -> np.array:
    """Applies a red filter by setting only the red channel and removing others."""
    red_array = array.copy()  # Make a copy to avoid modifying the original
    red_array[:, :, 1] = 0  # Set green channel to 0
    red_array[:, :, 2] = 0  # Set blue channel to 0
    return red_array  # Using = and *

def ft_green(array: np.array) -> np.array:
    """Applies a green filter by setting only the green channel and removing others."""
    green_array = array.copy()
    green_array[:, :, 0] = 0  # Set red channel to 0
    green_array[:, :, 2] = 0  # Set blue channel to 0
    return green_array  # Using = and -

def ft_blue(array: np.array) -> np.array:
    """Applies a blue filter by setting only the blue channel and removing others."""
    blue_array = array.copy()
    blue_array[:, :, 0] = 0  # Set red channel to 0
    blue_array[:, :, 1] = 0  # Set green channel to 0
    return blue_array  # Using only =

def ft_grey(array: np.array) -> np.array:
    """Converts the image to grayscale by averaging the RGB channels."""
    grey_array = array.mean(axis=2).astype(np.uint8)  # Average the three channels
    grey_array = np.stack((grey_array,) * 3, axis=-1)  # Stack to keep RGB format
    return grey_array  # Using = and /
