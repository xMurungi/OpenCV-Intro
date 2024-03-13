import os 
import cv2 as cv
import numpy as np

img_path = 'Pics/2023-06-01.png'

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
#resized = resized.astype(np.uint8)

b,g,r = cv.split(img)

cv.imshow("Blue", b)
cv.imshow("Green", g)
cv.imshow("Red", r)

print(resized.shape)
print(b.shape)
print(g.shape)
print(r.shape)
print("Number of channels in the original image:", resized.shape[2])

# Print the minimum and maximum values for each channel
print("Blue channel - min:", np.min(b), " max:", np.max(b))
print("Green channel - min:", np.min(g), " max:", np.max(g))
print("Red channel - min:", np.min(r), " max:", np.max(r))


cv.waitKey(0)