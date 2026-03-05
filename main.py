# Godwin Ofwono
# SEP23/BSE/3344U

from email.mime import image

import cv2
import numpy as np


# Task 1: Image Loading and Analysis

def task1():
    try:
        image = cv2.imread("Man.jpeg")

        if image is None:
            raise FileNotFoundError("Image not found!")

        height, width, channels = image.shape
        print("Image Dimensions:", image.shape)

        print("Data Type:", image.dtype)

        total_pixels = height * width
        print("Total Pixels:", total_pixels)

        print("Minimum Pixel Value:", image.min())
        print("Maximum Pixel Value:", image.max())

        center_pixel = image[height//2, width//2]
        print("Center Pixel(BGR) of Center Pixel:", center_pixel)

    except Exception as e:
        print("Error:", e)

# Task 2: Geometric Pattern Creation
def task2():
    img = np.zeros((600,600,3), dtype=np.uint8)

    center = (300, 300)

    # Outer red circle
    cv2.circle(img, center, 250, (0,0,255), 5)

    # Middle green circle
    cv2.circle(img, center, 150, (0,255,0), 5)

    # Inner blue circle (filled)
    cv2.circle(img, center, 50, (255,0,0), -1)

    # Diagonal line
    cv2.line(img, (0,0), (600,600), (255,255,255), 2)

    # Horizontal line
    cv2.line(img, (0,300), (600,300), (255,255,255), 2)

    cv2.putText(img, "TARGET", (200,580),
                cv2.FONT_HERSHEY_SIMPLEX,
                1, (255,255,255), 2)

    cv2.imwrite("task2_target.jpg", img)

# Task 3: Color Channel Manipulation 
#  
    # Original Image
    image = cv2.imread("Man.jpeg")


    b, g, r = cv2.split(image)

    #Image with Only Red Channel
    zeros = np.zeros_like(b)
    red_img = cv2.merge([zeros, zeros, r])

    cv2.imwrite("task3_red_channel.jpg", red_img)

    #Image with Only Green Channel

    zeros = np.zeros_like(b)
    green_img = cv2.merge([zeros, g, zeros])

    cv2.imwrite("task3_green_channel.jpg", green_img)

    #Image with Only Blue Channel
    zeros = np.zeros_like(b)
    blue_img = cv2.merge([b, zeros, zeros])

    cv2.imwrite("task3_blue_channel.jpg", blue_img)

    # reconstructing back to the original image
    reconstructed_img = cv2.merge([b, g, r])
    cv2.imwrite("task3_reconstructed.jpg", reconstructed_img)

# Task 4 : Color Space Conversion

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

gray_3ch = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

top = np.hstack((image, gray_3ch))
bottom = np.hstack((hsv, lab))
combined = np.vstack((top, bottom))

cv2.imwrite("task4_color_spaces.jpg", combined)


if __name__ == "__main__":
    # task1()
    task2()