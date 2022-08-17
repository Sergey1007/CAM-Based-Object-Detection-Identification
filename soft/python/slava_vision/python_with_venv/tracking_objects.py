from math import sqrt

import cv2
import time
import numpy as np
from yolo_detection_multi import multi_object_detect
import yolo_detection_multi


class Wheel():
    id=0

    def __init__(self,number_obj):
        self.coordinates=[0,0]
        self.queue=[]
        self.id_obj=number_obj

    def inspect(self,return_list):
        #all_coordinates = np.array(return_list, dtype='int16')
        all_coordinates=return_list[Wheel.id]
        print(all_coordinates)
        if all_coordinates != []:
            min_vector = 1000
            min_i=0
            i=0
            # if len(self.queue) < 3:
            #     x_obj, y_obj = self.coordinates
            # else:
            #     delta=[x-y for x,y in zip(self.coordinates,self.queue[-2])]
            #     x_obj,y_obj=[x+y for x,y in zip(self.coordinates,delta)]
            #     cv2.circle(img, (x_obj,y_obj), 10, (0, 255, 0), -1)

            x_obj, y_obj = self.coordinates
            for x, y in all_coordinates:
                cv2.circle(img, (x, y), 10, (0, 255, 0), -1)
                cv2.line(img, (width//2,0), (x, y), (0, 255, 0), thickness=2)
                vector = sqrt((x - x_obj) ** 2 + (y - y_obj) ** 2)
                i+=1
                if vector < min_vector:
                    min_vector = vector
                    minx, miny = x, y


                    min_i=i
            print(self.id_obj, minx, miny)
            self.coordinates = [minx, miny]
            all_coordinates.remove([minx,miny])

            cv2.putText(img,f'{self.id_obj}',self.coordinates,cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)
            if len(self.queue) < 3 and self.coordinates != []:
                self.queue.append(self.coordinates)
            else:
                self.queue.append(self.coordinates)
                del self.queue[0]
                for corrd in self.queue:
                    cv2.circle(img, corrd, 10, (0, 0, 255), thickness=1)





#config camera and port
cap = cv2.VideoCapture(0)
wheel1=Wheel(number_obj=1)
wheel2=Wheel(number_obj=2)
objects=[wheel1,wheel2]

height=480
width=640
count=0
counter=0

while True:
    _, img = cap.read()
    img = cv2.resize(img, (width,height))
    img = cv2.flip(img, 1)
    start = time.time()
    return_list = multi_object_detect(img)
    #all_coordinates=np.array(return_list,dtype=None)
    count+=1

    #print(all_coordinates)

    # if len(return_list[Wheel.id])==1:
    #     min_i=0
    #     i=0
    #     min_vector=1000
    #     x,y=return_list[Wheel.id][0]
    #     for object in objects:
    #         x_obj, y_obj = object.coordinates
    #         vector = sqrt((x - x_obj) ** 2 + (y - y_obj) ** 2)
    #         if vector < min_vector:
    #             min_vector = vector
    #             min_i = i
    #         i += 1
    #
    #     cv2.putText(img, f'{objects[min_i].id_obj}', (x,y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
    #     if len(objects[min_i].queue)<3:
    #         objects[min_i].queue.append([x,y])
    #     else:
    #         objects[min_i].queue.append([x,y])
    #         del objects[min_i].queue[0]
    #         for corrd in objects[min_i].queue:
    #             cv2.circle(img, corrd, 10, (0, 0, 255), thickness=1)
    #     for object in objects:
    #         if object.id_obj!=min_i+1 and count>3:
    #             object.coordinates=[0,0]
    #
    #             count=0
    #
    #
    # if len(return_list[Wheel.id])==1:
    #     counter+=1

    if len(return_list[Wheel.id])!=[]:
        print(return_list)
        if wheel2.coordinates==[0,0] and wheel1.coordinates!=[0,0]:
            wheel1.inspect(return_list=return_list)
            wheel2.inspect(return_list=return_list)
        if wheel1.coordinates == [0, 0] and wheel2.coordinates!=[0,0]:
            wheel2.inspect(return_list=return_list)
            wheel1.inspect(return_list=return_list)
        else:
            wheel1.inspect(return_list=return_list)
            wheel2.inspect(return_list=return_list)
        print(counter)
        print('--------------------')
        count=0

    end = time.time()
    cv2.putText(img, "{} fps".format(round(1 / (end - start), 2)), (20, 30), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 2)

    cv2.imshow("Image", img)
    cv2.waitKey(1)