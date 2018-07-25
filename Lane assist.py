# Imported libraries required for functions to operate efficiently
import cv2
import numpy as np

# Global variables
# Getting the video input
video_input = cv2.VideoCapture("test video.mp4")

# Blur pixel size
blur_size = 3

# Region of interest array with each [] representing x and y
points = np.array([[375, 0], [375, 0], [750, 135], [0, 135]], dtype=np.int32)
# Or
"""
trap_bottom_width = 0.85
trap_top_width = 0.07
trap_height = 0.4
imshape = image.shape
vertices = np.array([[ \
    ((imshape[1] * (1 - trap_bottom_width)) // 2, imshape[0]), \
    ((imshape[1] * (1 - trap_top_width)) // 2, imshape[0] - imshape[0] * trap_height), \
    (imshape[1] - (imshape[1] * (1 - trap_top_width)) // 2, imshape[0] - imshape[0] * trap_height), \
    (imshape[1] - (imshape[1] * (1 - trap_bottom_width)) // 2, imshape[0])]] \
    , dtype=np.int32)"""


# Functions required for the process of lane detection

"""
1. Region of interest :)
2. Filter colours     :)
3. grayscale          :)
4. Blur               :)
5. Canny edge         :(
6. Hough lines        :(
7. draw lines on the original image     :(
"""


def grayscale(frame):
    return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Applies the grayscale to the original image


def region_of_interest(frame, points):
    # The initial region if interest has to be sent as a frame
    # defining a blank mask to start with
    mask = np.zeros_like(frame)

    ignore_mask_color = 255, 255, 255

    # filling pixels inside the polygon defined by "vertices" with the fill color
    cv2.fillPoly(mask, [points], ignore_mask_color)

    # returning the image only where mask pixels are nonzero
    masked_image = cv2.bitwise_and(ROI, mask)
    return masked_image


def filter_colors(image):
    # Filter all the colours and leave colours only in the region of white and yellow
    # Filter white pixels
    white_threshold = 170
    lower_white = np.array([white_threshold, white_threshold, white_threshold])
    upper_white = np.array([255, 255, 255])
    white_mask = cv2.inRange(image, lower_white, upper_white)
    white_image = cv2.bitwise_and(image, image, mask=white_mask)

    # Filter yellow pixels
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower_yellow = np.array([90, 100, 100])
    upper_yellow = np.array([110, 255, 255])
    yellow_mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
    yellow_image = cv2.bitwise_and(image, image, mask=yellow_mask)

    # Combine the two above images
    image_filtered = cv2.addWeighted(white_image, 1., yellow_image, 1., 0.)

    return image_filtered


def gaussian_blur(image, blur_size):
    # blur the image for less noise
    return cv2.GaussianBlur(image, (blur_size, blur_size), 0)


# Main code
while True:
    check, frame = video_input.read()
    ROI = frame[500:635, 250:1000]  # region of interest initial cropped image
    cv2.imshow("Region of interest", region_of_interest(ROI, points))
    cv2.imshow("Filtered", filter_colors(region_of_interest(ROI, points)))
    cv2.imshow("Grayscale", grayscale(filter_colors(region_of_interest(ROI, points))))
    cv2.imshow("Blurred", gaussian_blur(grayscale(filter_colors(region_of_interest(ROI, points))), blur_size))
    cv2.imshow("orig", frame)

    key = cv2.waitKey(25)

    if key == ord('q'):
        break

video_input.release()
cv2.destroyAllWindows()
