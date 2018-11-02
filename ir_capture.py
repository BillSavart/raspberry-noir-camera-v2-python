import os
import sys
import subprocess
import cv2
import numpy as np

move = os.chdir("/home/pi/Pictures")
take_photo = subprocess.call("raspistill -o image.jpg", shell = True)

image = cv2.imread("image.jpg", -1)

des_image = cv2.namedWindow("Photo")
cv2.imshow("Photo", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
