import cv2
import numpy as np
from signal import make_signal
from yolo_detection import detect_object
import serial
import time
from arduino_uart import turn_motor

set_port=input("enter your com-port: ")
serialcomm = serial.Serial(set_port,115200)
serialcomm.timeout = 1
time.sleep(1)

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
    img = cv2.flip(img, 1)
    if fl:
        img = cv2.resize(img, (640, 480))
        old_coordinate = detect_object(img,output_layers_for_laser,net_laser)

old_coordinate=old_coordinate[0]
print(old_coordinate)
print('detection laser cycle exit')
signal=make_signal(old_coordinate,new_coordinate)
turn_motor(signal,serialcomm)
print(signal)




while True:
    cap = cv2.VideoCapture(0)
    fl, img = cap.read()
    img = cv2.flip(img, 1)
    if fl:
        img = cv2.resize(img, (640, 480))
        new_coordinate=detect_object(img,output_layers_for_wheel,net_wheel)
        if new_coordinate!=[]:
            new_coordinate=new_coordinate[0]
            signal=make_signal(old_coordinate,new_coordinate)
            turn_motor(signal, serialcomm)
            time.sleep(2)
            print('generate signal',signal)
            old_coordinate = new_coordinate




