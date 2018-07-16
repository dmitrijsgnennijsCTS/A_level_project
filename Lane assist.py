import cv2
import numpy as np


'#Create an object. zero for external camera'
video = cv2.VideoCapture(0)
a = 0


def make_customres():
    video.set(3, 1920)
    video.set(4, 1080)


while True:
    a = a+1
    '#Create a frame object'
    check, frame = video.read()

    #print(check)
    #print(frame)

    '#convert to grey scale'
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 75, 150) #find lines
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, 30, maxLineGap=250)
    print(lines)
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 3) #draw lines on the frame
    '#show the frame'
    cv2.imshow("Webcam1", edges)
    cv2.imshow("Webcam2", frame)

    '#Close when any key pressed(milliseconds)'
    key = cv2.waitKey(1)

    if key == ord('q'):
        break

print(a)
video.release()
cv2.destroyAllWindows()