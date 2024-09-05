#Refer - https://www.geeksforgeeks.org/opencv-python-tutorial/

#### Detection of Circles in a Image

"""import cv2
import numpy as np

img = cv2.imread('eyes.jpg', cv2.IMREAD_COLOR)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray_blurred = cv2.blur(gray, (3,3))

# Give a brief overview of what does HoughCirlces function do and What are the parameters required.
detected_circles = cv2.HoughCircles(gray_blurred, cv2.HOUGH_GRADIENT, 1, 20, param1 = 50, param2 = 30, minRadius = 1, maxRadius = 40)

if detected_circles is not None:
    detected_circles = np.uint16(np.around(detected_circles))
    for pt in detected_circles[0, :] :
        a, b, r = pt[0], pt[1], pt[2]
        cv2.circle(img, (a,b), r, (0, 255, 0), 2)
        cv2.circle(img, (a, b), 1, (0, 0, 255), 3)
        cv2.imshow("Detected Circles", img)
        cv2.waitKey(0)

cv2.destroyAllWindows()
"""

#### Count the number of circles in the image 
## Refer - https://www.geeksforgeeks.org/find-circles-and-ellipses-in-an-image-using-opencv-python/#

import cv2
import numpy as np
image = cv2.imread('pika.png', -1)

# Give a basic overview of the SimpleBlobDetecter function, Why it is used and What are the parameters required.

# Set our filtering parameters Initialize parameter settiing using cv2.SimpleBlobDetector
params = cv2.SimpleBlobDetector_Params()

# Set Area filtering parameters
#This is to avoid any identification of any small dots present in the image 
# that can be wrongly detected as a circle. 
#minArea: The minimum area of the blobs to be detected (in pixels).
            #  This helps in filtering out smaller blobs that are not of interest.
params.filterByArea = True
params.minArea = 100
# Set Circularity filtering parameters
#This helps us to identify, shapes that are more similar to a circle. 
params.filterByCircularity = True
params.minCircularity = 0.9

# Set Convexity filtering parameters
params.filterByConvexity = True
params.minConvexity = 0.2

# Set inertia filtering parameters
params.filterByInertia = True
params.minInertiaRatio = 0.01

# Create a detector with the parameters
detector = cv2.SimpleBlobDetector_create(params)
	
# Detect blobs
  # Each keypoint contains information 
# like the position and size of the blob.
keypoints = detector.detect(image)

#draw the circles around the blobs
                                  
blank = np.zeros((1, 1))
# cv2.drawKeypoints() draws the detected blobs on the original image.
# keypoints is the list of detected blobs.
# blank is a placeholder image that is not used in this case.
# (0, 0, 255) specifies the color of the circles (red in this case).
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures that the circles drawn represent the blobs' size.
blobs = cv2.drawKeypoints(image, keypoints, blank, (0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

#to display the count of blobs

number_of_blobs = len(keypoints)
text = "Number of Circular Blobs: " + str(len(keypoints))
cv2.putText(blobs, text, (20, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 100, 255), 2)

# cv2.putText() writes the number of detected blobs on the image.
# (20, 550) specifies the position on the image where the text should be placed.
# cv2.FONT_HERSHEY_SIMPLEX specifies the font type.
# 1 is the font scale, (0, 100, 255) is the color of the text (orange), and 2 is the thickness of the text

# Show blobs
cv2.imshow("Filtering Circular Blobs Only", blobs)
cv2.waitKey(0)
cv2.destroyAllWindows()


