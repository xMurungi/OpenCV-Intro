import cv2 as cv
import numpy as np

#img = cv.imread("Pics/2023-02-10 (8).png")
#cv.imshow("Valorant", img)

blank = np.zeros((500,900,3), dtype='uint8')
# cv.imshow("Blank", blank)


#                             1. PAINTING THE IMAGE A CERTAIN COLOR
# blank[200:300, 300:400] = 0,255,255
# cv.imshow("Blank", blank)


#                             2. DRAW A RECTANGLE
# thickness=cv.FILLED / thickness=-1 fills rectangle with color thickness=2 gives border thickness of 2
# cv.rectangle(blank, (100,50), (600,150), (0,255,0), thickness=cv.FILLED)
# cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=cv.FILLED) #half of original image
# cv.imshow("Rectangle", blank)


#                              3. DRAWING A CIRCLE
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 200, (0,255,255), thickness=-1)
cv.imshow("Circle", blank)

#                             4. DRAW A LINE
# thickness=cv.FILLED / thickness=-1 fills rectangle with color thickness=2 gives border thickness of 2
cv.line(blank, (257,200), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=3) #half of original image
cv.imshow("Line", blank)

#                              3. WRITING TEXT ON IMAGE
cv.putText(blank, "Hey, I am Joses!!", (0,100), cv.FONT_HERSHEY_TRIPLEX, 1.0, (100,55,105), thickness=2 )
cv.imshow("Text", blank)

cv.waitKey(0)
cv.destroyAllWindows()