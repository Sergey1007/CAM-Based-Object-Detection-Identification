import get_start_point as st
import cv2
from matplotlib import pyplot
from color_detection import get_red_xy


old_coordinate=[]
new_coordinate=[]
diff=[0,0]

img = cv2.imread('sources/laser3.jpg')
old_coordinate=st.get_start_xy(img)

print(old_coordinate)
cv2.circle(img, old_coordinate, 10, (255, 0, 0), -1) #you can draw a found point
#pyplot.imshow(img)
#pyplot.show()


img = cv2.imread('sources/ipad1.jpg')
new_coordinate=get_red_xy(img)
print(new_coordinate)
diff[0]=new_coordinate[0]-old_coordinate[0]
diff[1]=new_coordinate[1]-old_coordinate[1]
print(diff)

#print(diff)