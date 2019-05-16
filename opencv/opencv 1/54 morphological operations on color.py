import cv2
import matplotlib.pyplot as plt
import numpy as np

def main():
	
	path = "C:\\Users\\spars\\OneDrive\\Pictures\\set\\"
	#imgpath1 = path + "gray21.512.tiff"
	imgpath1 = path + "4.2.07.tiff"
	#imgpath1 = path + "5.1.09.tiff"
	#imgpath1 = path + "cameraman.tif"

	img = cv2.imread(imgpath1, 1)
	img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

#	th = 50 
#	max_val = 255
#	ret, o2 = cv2.threshold(img, th, max_val, cv2.THRESH_BINARY_INV)

#	k = np.ones((5,5),np.uint8)	
#	k = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
#	k = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
	k = cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))
	print(k)

	erosion = cv2.erode(img, k , iterations = 1)  

	dilation = cv2.dilate(img, k , iterations = 1) 	

	gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT,k)

	output = [img,erosion,dilation, gradient]
	titles = ['Original','erosion','dilation', 'gradient']

	for i in range(4):
		plt.subplot(2, 2, i+1)
		plt.imshow(output[i],cmap ='gray')
		plt.title(titles[i])
		plt.xticks([])
		plt.yticks([])
	plt.show()

if __name__ == "__main__":
	main()