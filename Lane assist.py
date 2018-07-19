import cv2
import numpy as np

'#Create an object. zero for external camera'
video = cv2.VideoCapture("test video.mp4")


while True:
    '#Create a frame object'
    check, frame = video.read()
    ROI = frame[470:635, 350:900] #region of interest
    cv2.imshow("Region of interest", ROI)
    hsv = cv2.cvtColor(ROI, cv2.COLOR_BGR2HSV)
    #hue sat value
    lower_yellow = np.array([0, 0, 100])
    upper_yellow = np.array([180, 130, 255])

    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
    res = cv2.bitwise_and(ROI, ROI, mask=mask)
    cv2.imshow("hsv", res)
    '#Close when any key pressed(milliseconds)'
    key = cv2.waitKey(25)

    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()