import cv2
import numpy as np
import matplotlib.pyplot as plt

def add_uniform_noise(image, noise_level):
    uniform_noise = np.random.uniform(-noise_level, noise_level, image.shape)
    noisy_image = image + uniform_noise
    return noisy_image

def reduce_noise(image, noise_reduction_percentage):
    return image * (1 - noise_reduction_percentage / 100)

def main():
    # Load the image
    image_path = 'image.jpg'
    image = cv2.imread(image_path)

    # Get values from the user
    noise_level = float(input("Enter the noise level for the Uniform noise: "))
    noise_reduction_percentage = float(input("Enter the noise reduction percentage: "))

    # Apply Uniform noise to each color channel
    noisy_image = np.zeros(image.shape, dtype=np.float32)
    for i in range(3):  # Loop through R, G, B channels
        noisy_image[:, :, i] = add_uniform_noise(image[:, :, i], noise_level)

    # Reduce noise in each color channel
    reduced_noise_image = np.zeros(image.shape, dtype=np.float32)
    for i in range(3):  # Loop through R, G, B channels
        reduced_noise_image[:, :, i] = reduce_noise(noisy_image[:, :, i], noise_reduction_percentage)

    # Convert images back to uint8
    noisy_image = np.clip(noisy_image, 0, 255).astype(np.uint8)
    reduced_noise_image = np.clip(reduced_noise_image, 0, 255).astype(np.uint8)

    # Display images using matplotlib
    plt.figure(figsize=(15, 5))

    plt.subplot(1, 3, 1)
    plt.title('Original Image')
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.title('Noisy Image')
    plt.imshow(cv2.cvtColor(noisy_image, cv2.COLOR_BGR2RGB))
    plt.axis('off')

    plt.subplot(1, 3, 3)
    plt.title('Reduced Noise Image')
    plt.imshow(cv2.cvtColor(reduced_noise_image, cv2.COLOR_BGR2RGB))
    plt.axis('off')

    plt.show()

if __name__ == "__main__":
    main()
