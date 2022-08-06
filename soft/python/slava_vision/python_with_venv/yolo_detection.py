import cv2
import numpy as np
import time

def detect_object(img,output_layers,net1):
    start=time.time()
    height, width, channels = img.shape

    # Detecting objects
    blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)

    net1.setInput(blob)
    outs = net1.forward(output_layers)

    #create lists with object
    class_ids = []
    confidences = []
    boxes = []
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.3:
                # Object detected
                #print(class_id)
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                # Rectangle coordinates
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    #sort out data
    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
    #font = cv2.FONT_HERSHEY_PLAIN
    final_coordinates=[]

    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h= boxes[i]
            x_c=x+w//2
            y_c=y+h//2
            final_coordinates.append([x_c,y_c])

            #label = str(classes[class_ids[i]])
            #color = colors[class_ids[i]]
            #cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
            #cv2.putText(img, label, (x, y + 30), font, 3, color, 2)
            cv2.circle(img,(x_c,y_c),10,(0,0,255),-1)

    end=time.time()
    print("fps is {}".format(1/(end-start)))
    cv2.imshow("Image", img)
    cv2.waitKey(1)
    return final_coordinates

if __name__=='__main__':
    #config yolo

    # net1 = cv2.dnn.readNet("wheel-tiny.weights", "yolov4-tiny-custom.cfg")
    net1 = cv2.dnn.readNet("multi.weights", "tiny_multi.cfg")
    classes = ["object","object1"]
    layer_names = net1.getLayerNames()
    output_layers = [layer_names[i - 1] for i in net1.getUnconnectedOutLayers()]
    #colors = np.random.uniform(0, 255, size=(len(classes), 3))


    cap = cv2.VideoCapture(0)
    _,img=cap.read()
    img = cv2.resize(img, (640, 480))
    while True:
        _, img = cap.read()
        img = cv2.resize(img, (640, 480))
        coordinates=detect_object(img,output_layers,net1)
        #coordinates=detect_object(img)
        print(coordinates)

