# Real-Time Multiple Color Detection Using OpenCV

This project uses OpenCV in Python to demonstrate real-time detection of multiple colors (red, green, and blue). The application captures video from the webcam, processes each frame to identify specified color ranges, and displays bounding boxes and labels around detected colors.

## Features
- Real-time video processing from the webcam
- Detection of red, green, and blue colors based on HSV color space
- Displays bounding boxes and labels for detected colors
- Easily configurable color ranges for detecting additional colors

## Requirements
- Python 
- OpenCV
- Numpy

## How It Works
The application captures each frame from the webcam and converts it to the HSV color space. It then applies color thresholds to create binary masks for each color (red, green, and blue). Using these masks, the script detects contours and draws bounding boxes around the areas where each color is detected.

This project is useful for demonstrating basic color-based object detection and tracking using OpenCV. You can also adjust the color ranges in HSV to detect other colors.
