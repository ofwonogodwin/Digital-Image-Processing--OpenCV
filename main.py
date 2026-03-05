import cv2
import numpy as np

def task1():
    try:
        image = cv2.imread("Man.jpeg")

        if image is None:
            raise FileNotFoundError("Image not found!")

        height, width, channels = image.shape
        print("Dimensions:", image.shape)

        print("Data Type:", image.dtype)

        total_pixels = height * width
        print("Total Pixels:", total_pixels)

        print("Min Pixel Value:", image.min())
        print("Max Pixel Value:", image.max())

        center_pixel = image[height//2, width//2]
        print("Center Pixel (BGR):", center_pixel)

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    task1()
    #task2()
    #task3()