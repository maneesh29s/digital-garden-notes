#!/usr/bin/env python

import argparse
import os
import platform
import yaml
from datetime import datetime


def read_file(filepath: str) -> list[str]:
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.readlines()


def write_file(filepath: str, content: list[str]) -> None:
    with open(filepath, 'w', encoding='utf-8') as file:
        file.writelines(content)


def get_file_birth_time(filepath: str) -> str:
    if platform.system() == 'Windows':
        import win32file
        import pywintypes

        handle = win32file.CreateFile(
            filepath, win32file.GENERIC_READ, win32file.FILE_SHARE_READ,
            None, win32file.OPEN_EXISTING, win32file.FILE_ATTRIBUTE_NORMAL, None
        )
        birth_time = win32file.GetFileTime(handle)[0]
        return datetime.fromtimestamp(birth_time.timestamp()).strftime('%Y-%m-%d')
    else:
        stat = os.stat(filepath)
        if hasattr(stat, 'st_birthtime'):
            return datetime.fromtimestamp(stat.st_birthtime).strftime('%Y-%m-%d')
        else:
            # Fallback for systems without st_birthtime
            return datetime.fromtimestamp(stat.st_ctime).strftime('%Y-%m-%d')

def get_file_modified_time(filepath: str) -> str:
    stat = os.stat(filepath)
    return datetime.fromtimestamp(stat.st_mtime).strftime('%Y-%m-%d')

def get_h1_title_or_filename(lines: list[str], filepath: str) -> str:
    for line in lines:
        if line.startswith('# '):
            return line[2:].strip()
    return os.path.basename(filepath)


def parse_frontmatter(lines: list[str]) -> tuple[dict, int]:
    if lines[0].strip() == '---':
        end = 1
        while end < len(lines) and lines[end].strip() != '---':
            end += 1
        if end < len(lines):
            frontmatter = yaml.safe_load(''.join(lines[1:end]))
            if frontmatter is not None:
                return frontmatter, end + 1
    return {}, 0


def build_frontmatter(frontmatter: dict) -> list[str]:
    return ['---\n', yaml.dump(frontmatter, default_flow_style=False), '---\n\n']


def ensure_frontmatter(filepath: str, dry_run: bool = False, new_tags: list[str] = None, new_aliases: list[str] = None) -> None:
    lines = read_file(filepath)
    frontmatter, content_start = parse_frontmatter(lines)

    existing_frontmatter = yaml.dump(frontmatter, default_flow_style=False)

    if 'title' not in frontmatter or frontmatter['title'] is None:
        frontmatter['title'] = get_h1_title_or_filename(lines[content_start:], filepath)

    if 'created' not in frontmatter or frontmatter['created'] is None:
        frontmatter['created'] = get_file_birth_time(filepath)

    if 'modified' not in frontmatter or frontmatter['modified'] is None:
        frontmatter['modified'] = get_file_modified_time(filepath)

    # Special condition to remove date
    if 'date' in frontmatter:
        del frontmatter['date']

    if 'author' not in frontmatter or frontmatter['author'] is None:
        frontmatter['author'] = "Maneesh Sutar"

    if 'aliases' not in frontmatter or frontmatter['aliases'] is None:
        frontmatter['aliases'] = []

    if 'tags' not in frontmatter or frontmatter['tags'] is None:
        frontmatter['tags'] = []
    
    # Add new aliases if provided
    if new_aliases:
        frontmatter['aliases'].extend(
            alias for alias in new_aliases if alias not in frontmatter['aliases'])

    if new_tags:
        frontmatter['tags'].extend(
            tag for tag in new_tags if tag not in frontmatter['tags'])

    # A special check to remove "public" tag if frontmatter already contains "private" tag
    # Can be removed if this check is not required in the future
    if "private" in frontmatter['tags'] and "public" in frontmatter['tags'] :
        frontmatter['tags'].remove("public")

    new_frontmatter_content = build_frontmatter(frontmatter)
    new_content = new_frontmatter_content + lines[content_start:]
    new_frontmatter = yaml.dump(frontmatter, default_flow_style=False)

    if dry_run:
        print(f"Existing frontmatter for {filepath}:\n\n{existing_frontmatter}")
        print(f"New frontmatter for {filepath}:\n\n{new_frontmatter}")
    else:
        if new_frontmatter != existing_frontmatter:
            print(f"Modifying frontmatter in {filepath}.")
            write_file(filepath, new_content)
        else:
            print(f"No changes made in {filepath}.")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Ensure consistent front matter in a Markdown file.")
    parser.add_argument('filepath', help="Path to the Markdown file.")
    parser.add_argument('-d', '--dry-run', action='store_true',
                        help="Preview changes without modifying files.")
    parser.add_argument(
        '-t', '--tags', help="Comma-separated list of new tags to add.", type=lambda s: s.split(','))
    parser.add_argument(
        '-a', '--aliases', help="Comma-separated list of new aliases to add.", type=lambda s: s.split(','))
    args = parser.parse_args()

    ensure_frontmatter(args.filepath, args.dry_run, args.tags, args.aliases)


if __name__ == "__main__":
    main()
