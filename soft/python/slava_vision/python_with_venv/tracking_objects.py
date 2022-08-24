from math import sqrt
from threading import Thread

import cv2
import time
import numpy as np
from yolo_detection_multi import multi_object_detect
import yolo_detection_multi
from signal import make_signal
from custom_uart import connect_to_serialport , transmit_string_with_receive

class Object():

    def __init__(self,number_obj):
        self.coordinates = [width//2+30*(number_obj-1), height//2]
        self.id_obj = number_obj
        self.find = False


class Wheel(Object):
    id=0

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

class Laser(Object):
    id = 1

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)



def sort_coordinates(data,objects,img):
    for x,y in data[objects[0].id]:
        cv2.circle(img, (x, y), 10, (0, 0, 255), -1)
        ind_find=0
        min_vector=sqrt(height**2+width**2)
        for object in objects:
            if object.find==False:
                x_obj,y_obj=object.coordinates
                vector=sqrt((x-x_obj)**2+(y-y_obj)**2)
                if vector<min_vector:
                    min_vector=vector
                    ind_find=object.id_obj
        #print(min_vector,ind_find)
        if objects[ind_find - 1].find == False:
            objects[ind_find-1].coordinates=[x,y]
            objects[ind_find-1].find=True

    for object in objects:
        object.find=False
        cv2.putText(img, str(object.id_obj), object.coordinates, cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 2)



def tracking_object():
    while True:
        _, img = cap.read()
        img = cv2.resize(img, (width,height))
        img = cv2.flip(img, 1)
        start = time.time()
        return_list = multi_object_detect(img)

        sort_coordinates(data=return_list,objects=wheels,img=img)
        sort_coordinates(data=return_list, objects=lasers,img=img)



        end = time.time()
        cv2.putText(img, "{} fps".format(round(1 / (end - start), 2)), (20, 30), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 2)
        cv2.imshow("Image", img)
        cv2.waitKey(1)


def send_signal():
    while True:
        print(lasers[0].coordinates, wheels[0].coordinates)
        signal = make_signal(lasers[0].coordinates, wheels[0].coordinates,installation=1)
        time.sleep(0.2)
        transmit_string_with_receive(signal)
        time.sleep(0.1)
        # print(lasers[1].coordinates, wheels[1].coordinates)
        # signal = make_signal(lasers[1].coordinates, wheels[1].coordinates, installation=2)
        # time.sleep(0.2)
        # transmit_string_with_receive(signal)
        # time.sleep(0.1)
        #print(signal)
        print('++++++++++++')

if __name__=='__main__':

    # config camera and port
    cap = cv2.VideoCapture(0)
    id_objects = {'wheel': 0, 'laser': 1}
    # connect_to_serialport()
    height = 480
    width = 640

    wheels = []
    lasers = []
    for i in range(1, 3):
        wheels.append(Wheel(number_obj=i))

    lasers.append(Laser(number_obj=1))



    thread1=Thread(target=tracking_object)
    thread1.start()
    # thread2 = Thread(target=send_signal())
    # thread2.start()