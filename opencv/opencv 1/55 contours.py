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

	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

	ret, thresh = cv2.threshold(gray,40,255,0)

	contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

	print(contours)
	print(hierarchy)

	cv2.drawContours(img, contours,-1,(0,0,255),2)

	Original = cv2.imread(imgpath1, 1)
	Original = cv2.cvtColor(Original,cv2.COLOR_BGR2RGB)

	output = [Original , img]
	titles = ['Original','thresh']

	for i in range(2):
		plt.subplot(1, 2, i+1)
		plt.imshow(output[i])
		plt.title(titles[i])
		plt.xticks([])
		plt.yticks([])
	plt.show()

if __name__ == "__main__":
	main()
