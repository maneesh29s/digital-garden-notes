#!/usr/bin/env bash

set -e

if [[ $# -lt 1 ]]
then
	echo "This script will sync your vaults content to the digital garden"
	echo "You can specify which folder/file to sync, with its path relative to the vault root."
	echo "note: this script has to be run from the root of your vault"
	echo
	echo "Usage: $0 <folder or file to sync>"
	echo
	echo "Currently you have not specified any folder, thus this script will sync entire vault, following the .export-ignore rules"
	echo "press enter to continue :)"
	read 
fi

START_AT=$1
OBSIDIAN_ROOT=$PWD
DIGITAL_GARDEN_ROOT=$HOME/opensource/digital-garden-notes

if [[ ! -d $DIGITAL_GARDEN_ROOT ]]
then
	echo "ERROR: Please change your digital garden repo location in the script"
	echo "Make sure it is cloned from your github repo"
	exit 1
fi

conditional_delete() {
  local dir_path=$1

  # Check if directory exists
  if [[ -d $dir_path ]]; then
    # Check if directory is empty
    if [[ -z "$(ls -A ${dir_path})" ]]; then
      echo "Directory $dir_path is already empty."
    else
      echo "Emptying $dir_path except excluded items"
      # Iterate over all files and directories within the specified directory
      for item in "${dir_path}"/*; do
		# List of files and folders to exclude
		excluded_items=("README.md" "index.md" "notebooks" "scripts")
		if [[ ! "${excluded_items[@]}" =~ "$(basename $item)" ]]; then
			rm -r "$item"
		fi
      done
    fi
  else
    echo "Directory $dir_path does not exist, nothing to delete."
  fi
}

# running obsidian-export
if [[ -z $START_AT ]] # on the entire vault
then
	conditional_delete $DIGITAL_GARDEN_ROOT
	echo "Emptied $DIGITAL_GARDEN_ROOT"
	obsidian-export --hard-linebreaks --skip-tags private $OBSIDIAN_ROOT $DIGITAL_GARDEN_ROOT
	echo "Notes have been exported to $DIGITAL_GARDEN_ROOT"
else # only export subfolder
	OUTPUT_PATH="$DIGITAL_GARDEN_ROOT/$START_AT"
	if [[ -d $OUTPUT_PATH ]]
	then
		conditional_delete $OUTPUT_PATH
		echo "Emptied $OUTPUT_PATH"
	else
		echo "Creating new directory $OUTPUT_PATH"
		mkdir -p "$OUTPUT_PATH"
	fi
	obsidian-export --hard-linebreaks --skip-tags private --start-at $OBSIDIAN_ROOT/$START_AT $OBSIDIAN_ROOT $OUTPUT_PATH
	echo "Notes have been exported to $OUTPUT_PATH"
fi

