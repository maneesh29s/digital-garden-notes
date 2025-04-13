#!/usr/bin/env python

import argparse
import re
import os

# Converts all wikilinks in the markdown file (to other notes or artifacts) to markdown style relative links
# it searches through the obsidian_base_directory for a matching file name


def convert_wikilinks_to_relative_links(
    file_path: str,
    obsidian_base_directory: str,
    convert_notes: bool,
    convert_artifacts: bool,
    dry_run: bool = False,
) -> None:
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    # Define the pattern for Wikilinks with aliases
    wikilink_pattern = r"\[\[([^\|\]]+)(?:\|([^\]]+))?\]\]"

    # Find all Wikilinks in the content
    matches = re.finditer(wikilink_pattern, content)

    # Track changes for dry run
    changes = []

    # Iterate through each match and convert it to a relative link
    for match in matches:
        # The existing link
        old_link = match.group(0)
        # separating page_name and alias
        page_name = match.group(1)
        alias = match.group(2)

        # Combine the page name and alias (if present) to form the link text
        link_text = alias if alias else page_name

        # Check if the link points to a markdown file (should have no extension)
        is_markdown_file = not os.path.splitext(page_name)[1]

        if is_markdown_file and not convert_notes:
            continue
        if not is_markdown_file and not convert_artifacts:
            continue

        # Find the full path to the target note or artifacts
        target_path = (
            find_note_path(obsidian_base_directory, page_name)
            if is_markdown_file
            else find_artifact_path(obsidian_base_directory, page_name)
        )

        if target_path is not None:
            # Build the relative path
            relative_path = os.path.relpath(target_path, os.path.dirname(file_path))
            new_link = f"[{link_text}]({relative_path})"
            changes.append((old_link, new_link))
        else:
            print(f"WARN: can not find target links for: {old_link}. Skipping.")

    if len(changes) == 0:
        print(f"NO changes to be made in {file_path}")
        return

    if dry_run:
        print(f"Changes to be made in {file_path}:")
        for old_link, new_link in changes:
            print(f"  Replace: {old_link}")
            print(f"     With: {new_link}")
    else:
        # Make the actual changes to the content
        for old_link, new_link in changes:
            content = content.replace(old_link, new_link)
        # Save the modified content back to the file
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(content)
        print(f"Wikilinks in {file_path} have been converted to relative links.")


def find_artifact_path(base_directory: str, target_name: str) -> str | None:
    for root, _, files in os.walk(base_directory):
        for file in files:
            if file == target_name:
                return os.path.join(root, file)
    return None


def find_note_path(base_directory, target_note) -> str | None:
    for root, _, files in os.walk(base_directory):
        for file in files:
            if file == f"{target_note}.md":
                return os.path.join(root, file)
    return None


def main() -> None:
    """
    Main function
    """
    parser = argparse.ArgumentParser(
        description="Convert Wikilinks in Obsidian Markdown files to relative links. You must select which types of links to convert using the optional arguments."
    )
    parser.add_argument(
        "obsidian_file_path", type=str, help="Path to the Obsidian Markdown file"
    )
    parser.add_argument(
        "obsidian_base_directory",
        type=str,
        help="Path to the base directory of the Obsidian vault",
    )
    parser.add_argument(
        "-n",
        "--notes",
        action="store_true",
        help="Convert links to other markdown notes",
    )
    parser.add_argument(
        "-a",
        "--artifacts",
        action="store_true",
        help="Convert links to other artifacts",
    )
    parser.add_argument(
        "-d",
        "--dry-run",
        action="store_true",
        help="Preview changes without modifying files.",
    )

    args = parser.parse_args()

    if not args.notes and not args.artifacts:
        print("No conversion option provided. Use --notes, --artifacts, or both.")
        return

    convert_wikilinks_to_relative_links(
        args.obsidian_file_path,
        args.obsidian_base_directory,
        args.notes,
        args.artifacts,
        args.dry_run,
    )


if __name__ == "__main__":
    main()
