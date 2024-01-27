#!/bin/sh -ex

# Split transcription columns into lines
python3 split_mdc_lines.py

# Render each transcription line
mdc2png/mdc2png ../mdc_lines/*.txt

# Move the rendered images to the expected directory
mkdir -p ../png_lines
mv ../mdc_lines/*.png ../png_lines/

# Build the website
python3 generate_webpage.py
