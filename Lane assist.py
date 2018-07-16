import cv2

'#Create an object. zero for external camera'
video = cv2.VideoCapture(0)
a = 0


while True:
    a = a+1
    '#Create a frame object'
    check, frame = video.read()

    #print(check)
    #print(frame)

    '#convert to grey scale'
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    '#show the frame'
    cv2.imshow("Webcam1", gray)
    cv2.imshow("Webcam2", frame)

    '#Close when any key pressed(milliseconds)'
    key = cv2.waitKey(1)

    if key == ord('q'):
        break

video.release()

cv2.destroyAllWindows()