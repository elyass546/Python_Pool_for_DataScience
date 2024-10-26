from PIL import Image
import numpy as np
import array
import matplotlib.pyplot as plt

def main():
    # image path is : "../ex02/*.jpg"
    pixel_data = ft_load("../ex02/animal.png")
    if pixel_data is not None:
        zoom_image(pixel_data)

def ft_load(path: str) -> np.array:
    try:
        # Load the image
        img = Image.open(path)

        # Convert to RGB format (if not already)
        img = img.convert("RGB")

        # Convert t
        # Trim the image (hardcoded values: top=450, left=100, height=400, width=400)
        image_trimmed = trim(pixel_data, 100, 400, 400, 400, 1)

        # Print new shape information after trimming
        print(f'The shape of image is: {image_trimmed.shape} or '
              f'({image_trimmed.shape[0]}, {image_trimmed.shape[1]})')
        print(image_trimmed)

        return image_trimmed

    except Exception as e:
        print(f"Error during zooming: {e}")

if __name__ == "__main__":
    main()