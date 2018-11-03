import os
import sys
import subprocess
import cv2
import numpy as np

file_name = sys.argv[1]

if len(sys.argv) == 4:
    file_path = sys.argv[3]
    move = os.chdir(file_path)
else:
    move = os.chdir("/home/pi/Pictures")

if len(sys.argv) == 3:
    int_argv = int(sys.argv[2])
    int_delay_time = (int_argv * 1000)
    delay_time = str(int_delay_time)
    command = "raspistill -o " + file_name + " -t " + delay_time
else:
    command = "raspistill -o " + file_name

take_photo = subprocess.call(command, shell = True)

image = cv2.imread(file_name, -1)

des_image = cv2.namedWindow("Photo")
cv2.imshow("Photo", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
