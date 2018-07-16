import cv2

'#Create an object. zero for external camera'
video = cv2.VideoCapture(0)
a = 0


def make_1080p():
    video.set(3, 1920)
    video.set(4, 1080)


def make_720p():
    video.set(3, 1280)
    video.set(4, 720)


def make_480p():
    video.set(3, 640)
    video.set(4, 480)


make_720p()


while True:
    a = a+1
    '#Create a frame object'
    check, frame = video.read()

    print(check)
    print(frame)

    '#convert to grey scale'
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    '#show the frame'
    cv2.imshow("Webcam1", frame)
    #cv2.imshow("Webcam2", frame)

    '#Close when any key pressed(milliseconds)'
    key = cv2.waitKey(1)

    if key == ord('q'):
        break

print(a)
video.release()
cv2.destroyAllWindows()