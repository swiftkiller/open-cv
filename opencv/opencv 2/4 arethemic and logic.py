import cv2
import numpy as np 
import matplotlib.pyplot as plt

imgpath = "C:\\Users\\spars\\OneDrive\\Pictures\\set\\"

img1 = cv2.imread(imgpath + "house.tiff")
img2 = cv2.imread(imgpath + "4.1.07.tiff")

img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

#add = img1 + img2
#imgadd = cv2.add(img1,img2) 
#weighted = cv2.addWeighted(img1,0.6,img2,0.4,0)
temp_img1 = img1
rows,cols,channels = img2.shape
roi = img1[0:rows,0:cols] 
img = cv2.add(roi,img2)

img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 150, 255,cv2.THRESH_BINARY_INV)
mask_inv = cv2.bitwise_not(mask)

img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv )
img2_fg = cv2.bitwise_and(img2,img2,mask=mask)

dst = cv2.add(img1_bg,img2_fg)
img1[0:rows,0:cols] = dst

titles = ['img2gray','mask_inv','mask','img1_bg','img2_fg','img1','temp_img1','image']
images = [img2gray,mask_inv,mask,img1_bg,img2_fg,img1,temp_img1,img] 

for i in range(8):
	plt.subplot(1, 8, i+1)
	plt.imshow(images[i])
	plt.title(titles[i])
	plt.xticks([])
	plt.yticks([])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()