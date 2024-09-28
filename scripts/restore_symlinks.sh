#!/bin/bash

# Find and restore deleted symbolic links
git ls-files --deleted | while read -r file; do
  # Check if the file was a symlink in the last commit
  if ( echo $file | grep -e "index.md" ) ; then
    echo "Restoring symlink: $file"
    git restore "$file"
  fi
done

echo "Restoration complete."
