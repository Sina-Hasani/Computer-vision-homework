import cv2 as cv 

# Specify the path to the image file
img_path = "img.jpg"

# Read the image from the specified path
img = cv.imread(img_path)

# Prompt the user to enter a zoom factor
zoom = float(input("Enter a number for zoom: "))

# Get the original width and height of the image
width, height = img.shape[:2]

# Calculate the new dimensions based on the zoom factor
new_width = int(zoom * width)    # New width after zooming
new_height = int(zoom * height)   # New height after zooming

# Resize the image to the new dimensions
zoomed_img = cv.resize(img, (new_width, new_height))

# Display image 
cv.imshow("Image", img)
cv.imshow("Zoomed image", zoomed_img)
cv.waitKey(0)
cv.destroyAllWindows()