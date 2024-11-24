import cv2
import matplotlib.pyplot as plt


image_path = 'image.jpg'  
img = cv2.imread(image_path)
img_copy = img.copy()

img_resized = cv2.resize(img_copy, (900, 900))
plt.imshow(cv2.cvtColor(img_resized, cv2.COLOR_BGR2RGB))
plt.axis('off')

pieces = []
height, width, _ = img_resized.shape
new_height = height // 3
new_width = width // 3


for i in range(3):
    for j in range(3):
        
        y_start = i * new_height
        y_end = (i + 1) * new_height
        x_start = j * new_width
        x_end = (j + 1) * new_width
        
        
        piece = img_resized[y_start:y_end, x_start:x_end]
        
        
        piece_resized = cv2.resize(piece, (100, 100))
        
        
        pieces.append(piece_resized)


fig, axes = plt.subplots(3, 3, figsize=(10, 10))
for i in range(3):
    for j in range(3):
        axes[i, j].imshow(cv2.cvtColor(pieces[i*3 + j], cv2.COLOR_BGR2RGB))  
        axes[i, j].axis('off')

plt.show()