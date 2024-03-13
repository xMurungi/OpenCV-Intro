import cv2 as cv

# img = cv.imread('Pics/2023-02-10 (8).png')
# cv.imshow("Valorant", img)

# cv.waitKey(0)

video = cv.VideoCapture("Videos/Serenity edit.mp4")

count = 0
while True:
    isTrue, frame = video.read()
    if not isTrue:
        break
    cv.imshow("Serenity", frame)
    
    count+=1
    
    if cv.waitKey(20) & 0xFF == ord('q'):
        break

print(count)
video.release()
cv.destroyAllWindows()
