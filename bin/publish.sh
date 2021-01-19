#!/bin/bash

# TODO: consider putting this in a file and using --exclude-from=FILE
EXCLUDES=()
#EXCLUDES+=(--exclude ".*")

rsync --verbose -avzh --delete --progress ./output/ "${EXCLUDES[@]}" paulkenn@paulmkennedy.com:~/www/blog/
