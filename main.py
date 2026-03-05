# Godwin Ofwono
# SEP23/BSE/3344U

from email.mime import image

import cv2
import numpy as np
import os


# Task 1: Image Loading and Analysis

def task1():
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

def task4():
    image = cv2.imread("Man.jpeg")
    h, w = image.shape[:2]

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

    gray = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

    image = cv2.resize(image, (400,400))
    gray = cv2.resize(gray, (400,400))
    hsv = cv2.resize(hsv, (400,400))
    lab = cv2.resize(lab, (400,400))

    top = np.hstack((image, gray))
    bottom = np.hstack((hsv, lab))
    combined = np.vstack((top, bottom))

    cv2.imwrite("task4_color_spaces.jpg", combined)

    # HSV best for red object detection (separates hue from lighting)
    # LAB better for skin detection (separates lightness from color)

#Task 5
def task5():
    image = cv2.imread("Man.jpeg")
    h, w = image.shape[:2]

    exact = cv2.resize(image, (400,300))

    half = cv2.resize(image, (w//2, h//2))

    new_w = 800
    new_h = int(h * (new_w / w))
    width_scaled = cv2.resize(image, (new_w, new_h))

    nearest = cv2.resize(image, (400,300), interpolation=cv2.INTER_NEAREST)
    linear = cv2.resize(image, (400,300), interpolation=cv2.INTER_LINEAR)
    cubic = cv2.resize(image, (400,300), interpolation=cv2.INTER_CUBIC)

    cv2.imwrite("task5_resized.jpg", half)

# Task 6
def rotate(image, angle):
    h, w = image.shape[:2]
    center = (w//2, h//2)

    M = cv2.getRotationMatrix2D(center, angle, 1.0)

    cos = abs(M[0,0])
    sin = abs(M[0,1])

    new_w = int((h*sin) + (w*cos))
    new_h = int((h*cos) + (w*sin))

    M[0,2] += (new_w/2) - center[0]
    M[1,2] += (new_h/2) - center[1]

    return cv2.warpAffine(image, M, (new_w, new_h))


def task6():
    image = cv2.imread("Man.jpeg")

    angles = [30,60,90,135,180]
    imgs = []

    for a in angles:
        r = rotate(image, a)
        r = cv2.resize(r, (400,400))
        cv2.putText(r, f"{a}°", (20,40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
        imgs.append(r)

    blank = np.zeros((400,400,3), dtype=np.uint8)

    top = np.hstack((imgs[0], imgs[1], imgs[2]))
    bottom = np.hstack((imgs[3], imgs[4], blank))

    final = np.vstack((top, bottom))

    cv2.imwrite("task6_rotations.jpg", final)

# Task 7
def task7():
    image = cv2.imread("Man.jpeg")
    h, w = image.shape[:2]

    center_crop = image[h//4:3*h//4, w//4:3*w//4]
    cv2.imwrite("task7_center_crop.jpg", center_crop)

    min_dim = min(h,w)
    square = image[0:min_dim, 0:min_dim]
    cv2.imwrite("task7_square_crop.jpg", square)

    roi = image[100:400, 100:400]
    cv2.imwrite("task7_roi_crop.jpg", roi)

    os.makedirs("task7_grid", exist_ok=True)

    cell_h = h//3
    cell_w = w//3

    for r in range(3):
        for c in range(3):
            cell = image[r*cell_h:(r+1)*cell_h,
                         c*cell_w:(c+1)*cell_w]

            cv2.imwrite(f"task7_grid/grid_row{r+1}_col{c+1}.jpg", cell)

# Task 8
def add_noise(image, amount=0.02):
    noisy = image.copy()
    h, w = image.shape[:2]
    num = int(amount*h*w)

    for _ in range(num):
        y = np.random.randint(0,h)
        x = np.random.randint(0,w)
        noisy[y,x] = [255,255,255]

    for _ in range(num):
        y = np.random.randint(0,h)
        x = np.random.randint(0,w)
        noisy[y,x] = [0,0,0]

    return noisy


def task8():
    image = cv2.imread("Man.jpeg")
    noisy = add_noise(image)

    avg = cv2.blur(noisy,(5,5))
    gauss = cv2.GaussianBlur(noisy,(5,5),0)
    median = cv2.medianBlur(noisy,5)
    bilateral = cv2.bilateralFilter(noisy,9,75,75)

    imgs = [noisy, gauss, median, bilateral]
    imgs = [cv2.resize(i,(400,400)) for i in imgs]

    top = np.hstack((imgs[0], imgs[1]))
    bottom = np.hstack((imgs[2], imgs[3]))

    final = np.vstack((top,bottom))

    cv2.imwrite("task8_blur_comparison.jpg", final)

    # Median best removes salt-pepper noise
    # Bilateral preserves edges best
    # Larger kernel = more blur, less detail

if __name__ == "__main__":
    # task1()
    # task2()
    task4()
    # task5()
    # task6()
    # task7()
    # task8()