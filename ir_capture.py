import os
import sys
import subprocess
import cv2
import numpy as np

move = os.chdir("/home/pi/Pictures")
argv = sys.argv[1]
command = "raspistill -o " + argv
take_photo = subprocess.call(command, shell = True)

image = cv2.imread("image.jpg", -1)

des_image = cv2.namedWindow("Photo")
cv2.imshow("Photo", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
