import cv2
import numpy as np 
import matplotlib.pyplot as plt 

imgpath = "C:\\Users\\spars\\OneDrive\\Pictures\\set\\house.tiff"
img = cv2.imread(imgpath, cv2.IMREAD_COLOR)

img[55,55]=[255,255,255]
px = img[55,55]
print(px)

roi=img[100:150,100:350] 
print(roi)
img[0:50,100:250] = [255,255,255]

car = img[300:420,60:430]

img[100:220, 60:430]=car
 

cv2.imshow('imgage',img)
cv2.waitKey(0)
cv2.destroyAllWindows()