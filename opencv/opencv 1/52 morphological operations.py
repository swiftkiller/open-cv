import cv2
import matplotlib.pyplot as plt
import numpy as np

def main():
	
	path = "C:\\Users\\spars\\OneDrive\\Pictures\\set\\"
	#imgpath1 = path + "gray21.512.tiff"
	#imgpath1 = path + "4.1.05.tiff"
	#imgpath1 = path + "5.1.09.tiff"
	imgpath1 = path + "cameraman.tif"

	img = cv2.imread(imgpath1, 0)

	th = 50 
	max_val = 255

	ret, o2 = cv2.threshold(img, th, max_val, cv2.THRESH_BINARY_INV)

#	k = np.ones((5,5),np.uint8)	
#	k = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
#	k = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
	k = cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))
	print(k)

	erosion = cv2.erode(o2, k , iterations = 3)  

	dilation = cv2.dilate(o2, k , iterations = 3) 	

	gradient = cv2.morphologyEx(o2, cv2.MORPH_GRADIENT,k)

	output = [img, o2,erosion,dilation, gradient]
	titles = ['Original','THRESH_BINARY_INV', 'erosion','dilation', 'gradient']

	for i in range(5):
		plt.subplot(2, 3, i+1)
		plt.imshow(output[i],cmap = 'gray')
		plt.title(titles[i])
		plt.xticks([])
		plt.yticks([])
	plt.show()

if __name__ == "__main__":
	main()
