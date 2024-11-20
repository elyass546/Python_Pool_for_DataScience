from PIL import Image
import numpy as np


def ft_load(path: str) -> np.array:
    try:
        # Load the image
        img = Image.open(path)

        # Convert to RGB format (if not already)
        img = img.convert("RGB")

        # Convert the image to a NumPy array for easier manipulation
        pixel_data = np.array(img)

        # Print the shape of the image (height, width, channels)
        print(f"The shape of the image is: {pixel_data.shape}")
        print(f"{pixel_data}")

        # Return the pixel data (or whatever you want)
        return pixel_data

    except FileNotFoundError:
        print("Error: The specified file was not found.")
    except IOError:
        print("Error: The file could not be opened.\
            Please ensure it is a valid image.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
