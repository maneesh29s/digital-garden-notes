#!/usr/bin/env python

import os
import re
import sys

# search and extracts all the wikilinks in all md files present in the given path
# and stores them in seperate extracted_wikilinks.md file
# such wikilinks can be converted to markdown links using wikilink_to_mdlink.py


def extract_wikilinks(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    # Define the pattern for Wikilinks with aliases
    wikilink_pattern = r"\[\[([^\|\]]+)(?:\|([^\]]+))?\]\]"

    # Find all Wikilinks in the content
    wikilinks = re.findall(wikilink_pattern, content)

    return wikilinks


def search_and_extract_wikilinks(base_directory, output_file):
    with open(output_file, "a", encoding="utf-8") as output:
        for root, _, files in os.walk(base_directory):
            for file in files:
                if file.endswith(".md"):
                    file_path = os.path.join(root, file)
                    wikilinks = extract_wikilinks(file_path)

                    if wikilinks:
                        output.write(f"## File path: {file_path}\n\n")
                        for page_name, alias in wikilinks:
                            output.write(f"Wikilink: {page_name}\n")
                            if alias:
                                output.write(f"  Alias: {alias}\n")
                            output.write("\n")
                        output.write("---\n\n")


if len(sys.argv) < 2:
    print(f"Usage: ${sys.argv[0]} path_to_obsidian_vault")
    exit(1)

obsidian_base_directory = sys.argv[1]  # Replace with the actual folder path

output_file_path = "extracted_wikilinks.md"

search_and_extract_wikilinks(obsidian_base_directory, output_file_path)
print(f"Wikilinks have been extracted and saved to {output_file_path}")
