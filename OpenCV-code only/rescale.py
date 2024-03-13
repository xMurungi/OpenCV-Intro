import os
import cv2 as cv

video_path = 'Videos/Serenity edit.mp4'

if not os.path.exists(video_path):
    print(f"Error: The file '{video_path}' does not exist.")
    # Handle the error or exit the script
else:
    capture = cv.VideoCapture(video_path)

def changeRes(width, height):
    # Live video only
    capture.set(3, width)
    capture.set(4, height)



def resize_video(frame, scale=0.55):
    # For live video, images and videos 
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

img = cv.imread("Pics/2023-02-10 (8).png")
resized_img = resize_video(img)
cv.imshow("Valorant", resized_img)

fps = capture.get(cv.CAP_PROP_FPS)

while True:
    isTrue, frame = capture.read()
    if not isTrue:
        break
    resized_vid = resize_video(frame)
    cv.imshow("Serenity", resized_vid)

    delay = int(1000 / fps)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cv.waitKey(0)
capture.release()    
cv.destroyAllWindows()