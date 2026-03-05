# Godwin Ofwono
# SEP23/BSE/3344U

import cv2
import numpy as np

# Task 1: Image Loading and Analysi

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


if __name__ == "__main__":
    task1()
    #task2()
    #task3()