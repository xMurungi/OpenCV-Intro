import os
import cv2 as cv
import numpy as np

img_path = 'Pics/dinosaur-record-long-neck.jpg'

if not os.path.exists(img_path):
    print(f"Error: The file '{img_path}' does not exist.")
    # Handle the error or exit the script
else:
    img = cv.imread(img_path)
    print(img_path + " is a valid path!")

def resize_image(frame, scale=0.90):
    # For live video, images and videos 
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

resized = resize_image(img)

#                         1. TRANSFORMING AN IMAGE 
# -x --> Shifting to the Left 
# -y --> Shifting to the Up
# x  --> Shifting to the Right
# y  --> Shifting to the Down

# def translate_image(img, x, y):
#     translateMatrix = np.float32([ [1,0,x], [0,1,y] ])
#     dimensions = (img.shape[1], img.shape[0])
#     return cv.warpAffine(img, translateMatrix, dimensions )

# translated_img = translate_image(resized, -200, 100)
# cv.imshow("Translated", translated_img)

# cv.waitKey(0)

#                         1. ROTATING AN IMAGE 
#  -angle --> clockwise
#  +angle --> anti-clockwise

# def rotate(image, angle, rotPoint=None):
#     (height, width) = image.shape[:2]
#     if rotPoint is None:
#         rotPoint = (width//2, height//2)

#     rotationMatrix = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
#     dimensions = (width, height)

#     return cv.warpAffine(image, rotationMatrix, dimensions)

# rotated = rotate(resized, 45)
# cv.imshow("Rotated", rotated)

# # cv.INTER_LINEAR cv.INTER_CUBIC --> expanding image 
# # cv.INTER_AREA --> shrinking image

# cv.waitKey(0)

#                         1. FLIPPING AN IMAGE 

flip = cv.flip(resized, -1)
cv.imshow("Flipped",flip)
# 0   --> flipped 180 vertically
# 1   --> flipped horizontally 
# -1  --> flipped horizontally and vertically
cv.waitKey(0)