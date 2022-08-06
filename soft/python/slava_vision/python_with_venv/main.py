import cv2
import numpy as np
from signal import make_signal
from yolo_detection import detect_object
import serial
import time
from custom_uart import connect_to_serialport , transmit_string




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
# new_coordinate=[640/2,480/2]
new_coordinate=[]



'''
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
connect_to_serialport()
transmit_string(signal)
print(signal)




while True:

    fl, img = cap.read()
    img = cv2.flip(img, 1)

    if fl:
        img = cv2.resize(img, (640, 480))
        start=time.time()
        new_coordinate=detect_object(img,output_layers_for_wheel,net_wheel)

        cv2.imshow("Image", img)
        end = time.time()
        print("in main {}".format(1 / (end - start)))
        cv2.waitKey(1)
        if new_coordinate!=[]:
            new_coordinate=new_coordinate[0]
            signal=make_signal(old_coordinate,new_coordinate)
            transmit_string(signal)
            time.sleep(1)
            print('generate signal',signal)
            old_coordinate = new_coordinate
'''

connect_to_serialport()
'''
kx=0
ky=0
while (kx==0 and ky==0):
    fl, img = cap.read()
    if fl:
            img = cv2.resize(img, (640, 480))
            img = cv2.flip(img, 1)
            old_coordinate = detect_object(img, output_layers_for_laser, net_laser)
            transmit_string("1 20 1 2 20 1")
            time.sleep(2)
            new_coordinate = detect_object(img, output_layers_for_laser, net_laser)
            cv2.imshow("camera",img)
            cv2.waitKey(1)
            print(old_coordinate)
            print(new_coordinate)
            if new_coordinate != [] and old_coordinate != []:
                old_coordinate = old_coordinate[0]
                new_coordinate = new_coordinate[0]
                kx=(new_coordinate[0]-old_coordinate[0])/20
                ky =(new_coordinate[1] - old_coordinate[1]) / 20
                print(old_coordinate)
                print(new_coordinate)
                print(kx)
                print(ky)
print("i'm here")
'''






i=0
while True:
    fl, img = cap.read()
    if fl:
        img = cv2.resize(img, (640, 480))
        img = cv2.flip(img, 1)
        old_coordinate = detect_object(img, output_layers_for_laser, net_laser)

        new_coordinate = detect_object(img, output_layers_for_wheel, net_wheel)
        cv2.imshow("Image", img)
        cv2.waitKey(1)
        if new_coordinate != [] and old_coordinate!=[]:
            old_coordinate = old_coordinate[0]
            if i==0:
                compare_coordinate=old_coordinate
                i=1
            if i!=0:
                pass


            new_coordinate = new_coordinate[0]
            print(type(new_coordinate[0]))
            print(type(new_coordinate[0]))

            signal = make_signal(old_coordinate, new_coordinate)
            transmit_string(signal)
            print(old_coordinate)
            print(new_coordinate)
            print('generate signal', signal)


