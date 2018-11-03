import os
import sys
import subprocess
import cv2
import numpy as np

ir_file_name = sys.argv[1]
flir_file_name = sys.argv[2]

move = os.chdir("pylepton/")

if len(sys.argv) == 4:
    int_argv = int(sys.argv[3])
    int_delay_time = (int_argv * 1000)
    delay_time = str(int_delay_time)
    command = "raspistill -o " + ir_file_name + " -t " + delay_time
else:
    command = "raspistill -o " + ir_file_name

take_ir_photo = subprocess.call(command, shell = True)
take_flir_photo = subprocess.call("./pylepton_capture " + flir_file_name, shell = True)

#OpenCV
image_ir = cv2.imread(ir_file_name, -1)
image_flir = cv2.imread(flir_file_name, 0)

image_flir = cv2.applyColorMap(image_flir, cv2.COLORMAP_JET)

des_image_ir = cv2.namedWindow("ir_photo")
des_image_flir = cv2.namedWindow("flir_photo")

cv2.imshow("ir_photo", image_ir)
cv2.imshow("flir_photo", image_flir)

cv2.waitKey(0)
cv2.destroyAllWindows()
