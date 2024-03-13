import os 
import cv2 as cv
import matplotlib.pyplot as plt

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

# HSV hue saturation value
hsv = cv.cvtColor(resized, cv.COLOR_BGR2HSV)
cv.imshow("HSV", hsv)

#                        LAB 
# lab = cv.cvtColor(resized, cv.COLOR_BGR2Lab)
# cv.imshow("lab", lab)
#  cv.COLOR_BGR2Lab 

#                         RGB
# rgb = cv.cvtColor(resized, cv.COLOR_BGR2RGB)
# cv.imshow("lab", rgb)

# plt.imshow(rgb)
# plt.show()

#                         HSV TO BGR 
# grayscale-bgr-lab
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow("HSV-BGR", hsv_bgr)

cv.waitKey(0)