import get_start_point as st
import cv2
import numpy as np
#from matplotlib import pyplot
#from color_detection import get_red_xy
from signal import make_signal



old_coordinate=[]
new_coordinate=[1280/2,920/2]

a=0
while (old_coordinate==[]):
    if (a==0):
        img = cv2.imread('sources/ipad1.jpg')

    if (a==1):
        img = cv2.imread('sources/laser3.jpg')
    a+=1
    img=cv2.resize(img,(1280,920))


    #cap = cv2.VideoCapture(0)
    #_, img = cap.read()
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
print(signal)
'''

while True:

    old_coordinate=new_coordinate
    #img = cv2.imread('sources/ipad1.jpg')
    cap = cv2.VideoCapture(0)
    fl, img = cap.read()
    if (fl==True):
        try:
            img = cv2.resize(img, (1280, 920))
            new_coordinate=get_red_xy(img)
            cv2.circle(img, new_coordinate, 10, (255, 0, 0), -1) #you can draw a found point
            signal=make_signal(old_coordinate,new_coordinate)
            print(signal)
            cv2.imshow('result',img)
            cv2.waitKey(1000)
        except ZeroDivisionError:
            print('error')
'''
