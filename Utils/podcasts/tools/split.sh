#!/bin/bash

# Check if an argument was provided
if [ -z "$1" ]; then
    echo "Error: No input MP3 file specified."
    echo "Usage: $0 <file.mp3>"
    exit 1
fi

INPUT="$1"

# Check if the file exists
if [ ! -f "$INPUT" ]; then
    echo "Error: File '$INPUT' does not exist."
    exit 1
fi

# Get the filename without the .mp3 extension
FILENAME_NO_EXT=$(basename "$INPUT" .mp3)

echo "Splitting '$INPUT' into 1-hour segments..."

# Run ffmpeg
# -i: input file
# -f segment: split mode
# -segment_time 3600: segment duration in seconds (1 hour)
# -segment_start_number 1: start numbering from 1 instead of 0
# -c copy: copy stream without re-encoding (fast and lossless)
ffmpeg -i "$INPUT" -f segment -segment_time 3600 -segment_start_number 1 -c copy "${FILENAME_NO_EXT}_part_%03d.mp3"

if [ $? -eq 0 ]; then
    echo "Success! Segments have been created."
else
    echo "Error: Something went wrong during the split process."
fi

