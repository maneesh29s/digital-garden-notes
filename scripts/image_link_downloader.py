#!/usr/bin/env python

import os
import re
import requests
import sys
from urllib.parse import urlparse


# if markdown file contains URLs of images on the internet,
# this script will download them, keep them in the "Artifacts" folder in the same directory as markdown file
# also will replace the URLs of the image in md file, with markdown styles relative links
def download_images_from_markdown(markdown_file):

    # Reading whole markdown file
    with open(markdown_file, "r") as file:
        markdown_content = file.read()

    # gettting only image urls from md file
    image_urls = re.findall("!\[[^\]]*\]\((http.*)\)", markdown_content)

    # base directory of both markdown file and the "Artifacts" folder
    base_directory = os.path.dirname(markdown_file)

    image_directory = os.path.join(base_directory, "Artifacts")
    os.makedirs(image_directory, exist_ok=True)

    # Generate sequential image names based on markdown filename
    base_image_name = os.path.splitext(os.path.basename(markdown_file))[0]
    image_counter = 0

    for url in image_urls:
        image_name = f"{base_image_name}_{image_counter}"
        image_name = image_name.replace(
            " ", "_"
        )  # Replace space characters with underscores

        parsed_url = urlparse(url)
        image_extension = os.path.splitext(parsed_url.path)[1]
        image_name_with_extension = f"{image_name}{image_extension}"

        # sanity check for jpeg extension
        image_name_with_extension = image_name_with_extension.replace(".jpg", ".jpeg")
        image_path = os.path.join(image_directory, image_name_with_extension)

        try:
            response = requests.get(url)
            if response.status_code != 200:
                print(
                    f"Request to {url} failed with status code: {response.status_code}"
                )
                continue
        except requests.RequestException as e:
            print(f"An error occurred: {e}")
            return

        with open(image_path, "wb") as image_file:
            image_file.write(response.content)

        print(f"Downloaded image: {image_name_with_extension}")

        relative_image_path = os.path.relpath(image_path, base_directory)
        markdown_image_link = f"![{image_name}]({relative_image_path})"

        markdown_content = re.sub(
            f"!\[[^\]]*\]\({re.escape(url)}\)", markdown_image_link, markdown_content
        )

        image_counter += 1

    # # Writing back to markdown file
    with open(markdown_file, "w") as file:
        file.write(markdown_content)

    print("All images downloaded and links updated successfully.")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} markdown_file_path")
        exit(1)

    markdown_file_path = sys.argv[1]

    download_images_from_markdown(markdown_file_path)
