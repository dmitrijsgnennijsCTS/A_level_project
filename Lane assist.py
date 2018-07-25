# Imported libraries required for functions to operate efficiently
import cv2

# Global variables
# Getting the video input
video_input = cv2.VideoCapture("test video.mp4")


# Functions required for the process of lane detection
def grayscale(frame):
    return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Applies the grayscale to the original image


# Main code
while True:
    check, frame = video_input.read()
    cv2.imshow("Grayscale", grayscale(frame))

    key = cv2.waitKey(25)

    if key == ord('q'):
        break

video_input.release()
cv2.destroyAllWindows()
