#!/usr/bin/env python

import re
import sys

# this program must be called after png images are converted to jpeg 
# using the image_png_to_jpeg.py program

# input is markdown file, which contains markdown style relative links to '.png' images
# replaces ' ' with '_', also changes extention to '.jpeg'
def replace_image_names(filename):
    with open(filename, 'r') as file:
        content = file.read()

    # Pattern to match Markdown-style image links
    markdown_pattern = r'!\[([^\]]*?)\]\((.*?\.png)\)'

    # Function to change .png to .jpeg in Markdown links
    def markdown_replacement(match):
        alt_text = match.group(1)
        image_name = match.group(2).replace(' ', '_').replace('.png', '.jpeg')
        return f'![{alt_text}]({image_name})'
    
    replaced_content = re.sub(markdown_pattern, markdown_replacement, content)

    with open(filename, 'w') as file:
        file.write(replaced_content)


if __name__=="__main__":
    if (len(sys.argv) < 2):
        print(f"Usage: {sys.argv[0]} markdown_file_path")
        exit(1)

    markdown_file_path = sys.argv[1]

    replace_image_names(markdown_file_path)
