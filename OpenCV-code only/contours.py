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

blank = np.zeros(resized.shape, dtype='uint8')
cv.imshow("Blank", blank)

#  boundaries of objects

gray = cv.cvtColor(resized, cv.COLOR_BGR2GRAY)
cv.imshow("Grayscale", gray)

blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow("Blurred", blur)

canny = cv.Canny(blur, 125, 175)
cv.imshow("Canny Edges", canny)

ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow("Threshold", thresh)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} contour(s) found!')

cv.drawContours(resized, contours, -1, (0,255,0), 1)
cv.imshow("Contours Drawn", resized)

# cv.RETR_TREE --> for all hierarchical contours
# cv.RETR_EXTERNAL --> external contours 
# cv.RETR_LIST --> all contours
cv.waitKey(0)