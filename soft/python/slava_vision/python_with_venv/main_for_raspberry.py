import get_start_point as st
import cv2
import numpy as np
from signal import make_signal
import smbus
import time
from i2c_block import send_arr

old_coordinate=[]
new_coordinate=[1280/2,920/2]

bus=smbus.SMBus(1)
SLAVE_ADDRESS=0x04

cap = cv2.VideoCapture(0)


while (old_coordinate==[]):
    fl, img = cap.read()
    #img=cv2.imread('sources/laser3.jpg')
    print(fl)
    try:
        old_coordinate=st.get_start_xy(img)
    except ZeroDivisionError:
        print('error')
        cv2.imshow('result', img)
        cv2.waitKey(3000)
    else:
        #print(old_coordinate)
        cv2.circle(img, old_coordinate, 10, (255, 0, 0), -1) #you can draw a found point
        cv2.imshow('result',img)
        cv2.waitKey(3000)

print(old_coordinate)
print('cycle exit')
signal=make_signal(old_coordinate,new_coordinate)
print(signal[:3])
print(signal[3:])

send_arr(signal[:3])
time.sleep(1)
send_arr(signal[3:])

print('programm exit')