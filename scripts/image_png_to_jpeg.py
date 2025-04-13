#!/usr/bin/env python

import os
import sys
from PIL import Image


# Works only on '.png' images
# replaces the ' ' with '_' if present in the name
# also converts them into '.jpeg'
def png_to_jpeg_converter(directory_path):
    for filename in os.listdir(directory_path):
        if filename.endswith(".png"):

            new_filename = filename.replace(" ", "_").replace(".png", ".jpeg")

            image_path = os.path.join(directory_path, filename)
            new_image_path = os.path.join(directory_path, new_filename)

            # Convert PNG to JPEG
            image = Image.open(image_path)
            image = image.convert("RGB")
            image.save(new_image_path, "JPEG")

            # Remove the original PNG file
            os.remove(image_path)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: ${sys.argv[0]} directory_containing_png_images")
        exit(1)

    directory_path = sys.argv[1]  # Replace with the actual folder path

    png_to_jpeg_converter(directory_path)
