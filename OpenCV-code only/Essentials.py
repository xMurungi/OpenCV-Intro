import cv2 as cv
import os


#                    1. CONVERTING TO GRAYSCALE 
img_path = 'Pics/2023-02-10 (8).png'

if not os.path.exists(img_path):
    print(f"Error: The file '{img_path}' does not exist.")
    # Handle the error or exit the script
else:
    img = cv.imread(img_path)

# cv.imshow("Spaceman", img)

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("Grayscale", gray)

# img_2 = cv.imread('Pics/2023-06-01.png')
# cv.imshow("img2", img_2)
# gray2 = cv.cvtColor(img_2, cv.COLOR_BGR2GRAY)
# cv.imshow("2", gray2)

# cv.waitKey(0)


#                     2. BLURRING

# blur = cv.GaussianBlur(img, (9,9), cv.BORDER_DEFAULT)
# cv.imshow("Blurred", blur)

# cv.waitKey(0)
    
#                      3. EDGE CASCADE
# canny = cv.Canny(img, 125, 175)
# cv.imshow("Canny Edges", canny)

#cv.waitKey(0)

#                       4. DILATING THE IMAGE 
# dilated = cv.dilate(canny, (9,9), iterations=5)
# cv.imshow("Dilated", dilated)

#cv.waitKey(0)

#                       5. ERODED
# eroded = cv.erode(dilated, (9,9), iterations=5)
# cv.imshow("Eroded", eroded)

# cv.waitKey(0)

#                       6. RESIZING AN IMAGE
# cv.INTER_LINEAR cv.INTER_CUBIC --> expanding image 
# cv.INTER_AREA --> shrinking image
    
# resized = cv.resize(img, (1200,700), interpolation=cv.INTER_CUBIC-->(not a must))
# cv.imshow("Resized", resized)

# cv.waitKey(0)
    
#                       7. CROPIING AN IMAGE 

cropped = img[100:200, 600:800]
cv.imshow("Cropped", cropped)

cv.waitKey(0)