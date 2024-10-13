import cv2
import numpy as np
import math

# Define image properties
width = 256
height = 256
n_channels = 3

# black background
img = np.zeros(shape=(width, height, n_channels), dtype=np.uint8)

# Define two points
x1 = 180; y1 = 150
x2 = 100; y2 = 220

# Calculate slope (m) and intercept (b) of the line y = mx + b
try:
    m = (y2 - y1) / (x2 - x1)
    b = y1 - m * x1
    print(f"Slope: {m}")
except Exception as e:
    print(f"Error: {e}")

# Function to calculate distance from a point (px, py) to the line y = mx + b
def distance_from_line(px, py, m, b):
        return abs(m * px - py + b) / math.sqrt(m**2 + 1)
    

# Set up color gradient based on distance to the line
max_distance = math.sqrt(width**2 + height**2)  # Maximum possible distance in the image

for i in range(width):
    for j in range(height):
        # Calculate distance from the current pixel to the line
        dist = distance_from_line(i, j, m, b)
        
        # Normalize the distance to a range of 0 to 1
        normalized_dist = dist / max_distance
        
        color = int(normalized_dist * 255)
        
        # Set the pixel color
        img[i, j] = [color, 0, (255 - color) * 0.6]
      
   
# Display the image
cv2.imshow('Image', img)
cv2.waitKey(0)
