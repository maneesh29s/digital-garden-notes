#!/usr/bin/env python

import argparse
import re
import os
from wikilink_to_mdlink import find_note_path

# This will only convert markdown links to other markdown files to wikilinks
# It will keep all other links as it is


def convert_markdown_links_to_wikilinks(file_path: str, dry_run: bool = False) -> None:
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Define the pattern for Markdown links
    markdown_link_pattern = r'\[([^\]]*)\]\(([^)]+)\)'

    # Find all Markdown links in the content using finditer to get match objects
    matches = re.finditer(markdown_link_pattern, content)

    # Track changes for dry run
    changes = []

    # Iterate through each match and convert it to a Wikilink
    for match in matches:
        # Entire match
        full_match = match.group(0)
        # Groups
        link_text = match.group(1).strip()
        link_target = match.group(2).strip()

        # Convert the target to a Wikilink if it points to a Markdown file
        if link_target.endswith('.md'):
            # sanity check to see if file really exists at the location
            if (link_target.startswith('/') and not os.path.exists(link_target)) or (not os.path.exists(os.path.join(os.path.dirname(file_path), link_target))):
                print(
                    f"WARN: the file {link_target} does not exist locally. Skipping")
                continue

            # Extract the page name from the link target
            page_name = os.path.splitext(os.path.basename(link_target))[0]

            # Construct the Wikilink with or without alias
            if not link_text or link_text == page_name:
                wikilink = f'[[{page_name}]]'
            else:
                wikilink = f'[[{page_name}|{link_text}]]'
            changes.append((full_match, wikilink))

    if len(changes) == 0:
        print(f'NO changes to be made in {file_path}')
        return
    
    if dry_run:
        print(f'Changes to be made in {file_path}:')
        for old_link, new_link in changes:
            print(f'  Replace: {old_link}')
            print(f'     With: {new_link}')
    else:
        # Make the actual changes to the content
        for old_link, new_link in changes:
            content = content.replace(old_link, new_link)
        # Save the modified content back to the file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        print(
            f'Markdown links in {file_path} have been converted to Wikilinks.')


def main() -> None:
    parser = argparse.ArgumentParser(
        description='Convert Markdown links (to other notes) in Markdown files to Wikilinks. This will not change links to other artifacts (images, pdfs) and external URLs')
    parser.add_argument('obsidian_file_path', type=str,
                        help='Path to the Obsidian Markdown file')
    parser.add_argument('-d', '--dry-run', action='store_true',
                        help="Preview changes without modifying files.")
    args = parser.parse_args()

    convert_markdown_links_to_wikilinks(args.obsidian_file_path, args.dry_run)


if __name__ == '__main__':
    main()
