import cv2
import numpy as np 
import matplotlib.pyplot as plt 

imgpath = "C:\\Users\\spars\\OneDrive\\Pictures\\set\\house.tiff"

img = cv2.imread(imgpath, cv2.IMREAD_GRAYSCALE)

cv2.imshow('imgage',img)
cv2.waitKey(0)
cv2.destroyAllWindows()