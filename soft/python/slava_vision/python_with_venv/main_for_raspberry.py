import cv2
import numpy as np
from signal import make_signal
import smbus
from i2c_block import send_arr
from yolo_detection import detect_object
import time

bus=smbus.SMBus(1)
SLAVE_ADDRESS=0x04


#config yolo for wheels
net_wheel = cv2.dnn.readNet("wheel-tiny.weights", "yolov4-tiny-custom.cfg")
classes = ["object"]
layer_names_wheel = net_wheel.getLayerNames()
output_layers_for_wheel = [layer_names_wheel[i - 1] for i in net_wheel.getUnconnectedOutLayers()]

#config yolo for laser
net_laser = cv2.dnn.readNet("laser.weights", "yolov3_custom.cfg")
classes = ["object"]
layer_names_laser = net_laser.getLayerNames()
output_layers_for_laser = [layer_names_laser[i - 1] for i in net_laser.getUnconnectedOutLayers()]

#config camera and start coordinates
cap = cv2.VideoCapture(0)
old_coordinate=[]
new_coordinate=[640/2,480/2]




while (old_coordinate==[]):
    fl,img=cap.read()
    if fl:
        img = cv2.resize(img, (640, 480))
        old_coordinate = detect_object(img,output_layers_for_laser,net_laser)

old_coordinate=old_coordinate[0]
print(old_coordinate)
print('detection laser cycle exit')
signal=make_signal(old_coordinate,new_coordinate)
print(signal)

send_arr(signal)
time.sleep(1)




while True:
    cap = cv2.VideoCapture(0)
    fl, img = cap.read()
    if fl:
        img = cv2.resize(img, (640, 480))
        new_coordinate=detect_object(img,output_layers_for_wheel,net_wheel)
        if new_coordinate!=[]:
            new_coordinate=new_coordinate[0]
            signal=make_signal(old_coordinate,new_coordinate)
            print('generate signal',signal)
            old_coordinate = new_coordinate
            send_arr(signal)
            time.sleep(0.5)






