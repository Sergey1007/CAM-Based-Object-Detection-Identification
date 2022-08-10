import cv2
import numpy as np
from signal import make_signal
import time
from custom_uart import connect_to_serialport , transmit_string
from yolo_detection_multi import multi_object_detect
import yolo_detection_multi
import enum

class Objects(enum.Enum):
    wheel = 0
    laser = 1

class Laser:
    coordinates=[]
    def __init__(self):
        self.coordinates=[0,0]

class Wheel():
    coordinates = []
    def __init__(self):
        self.coordinates = [0,0]

#config camera and port
cap = cv2.VideoCapture(0)
wheel=Wheel()
laser=Laser()
#connect_to_serialport()

while True:
    _, img = cap.read()
    img = cv2.resize(img, (640, 480))
    img = cv2.flip(img, 1)
    start = time.time()
    return_list = multi_object_detect(img)
    end = time.time()
    cv2.putText(img, "{} fps".format(round(1 / (end - start), 2)), (20, 30), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 2)


    if return_list[Objects.wheel.value]!=[]:
        print(return_list[Objects.wheel.value][0])
        wheel.coordinates=return_list[Objects.wheel.value][0]

    if return_list[Objects.laser.value]!=[]:
        print(return_list[Objects.laser.value][0])
        laser.coordinates = return_list[Objects.laser.value][0]

    if wheel.coordinates!=[] and laser.coordinates!=[]:
        signal = make_signal(laser.coordinates, wheel.coordinates)
        print('generate signal', signal)
        laser.coordinates = []
        wheel.coordinates = []






    cv2.imshow("Image", img)
    cv2.waitKey(1)


