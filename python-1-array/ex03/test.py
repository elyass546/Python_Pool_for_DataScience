from zoom import zoom_image
from load_image import ft_load


def main():
    try:
        # image path is : "../ex02/*.jpg"
        pixel_data = ft_load("../ex02/animal.png")
        if pixel_data is not None:
            zoom_image(pixel_data)
    except KeyboardInterrupt:
        print("\nProcess interrupted by user (Ctrl+C). Exiting gracefully...")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()