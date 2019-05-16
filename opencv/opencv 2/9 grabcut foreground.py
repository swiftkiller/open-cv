import cv2
import numpy as np
import matplotlib.pyplot as plt 

img = cv2.imread('C:\\Users\\spars\\OneDrive\\Pictures\\Camera Roll\\WIN_20170902_18_09_13_Pro.jpg')


mask = np.zeros(img.shape[:2],np.uint8)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

bgModel = np.zeros((1,65),np.float64)
fgModel = np.zeros((1,65),np.float64)

rect = (700,150,920,500)

cv2.grabCut(img,mask,rect,bgModel,fgModel,5,cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
img = img*mask2[:,:,np.newaxis]
plt.imshow(img)
plt.colorbar()
plt.show()
