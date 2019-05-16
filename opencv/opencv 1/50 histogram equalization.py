import cv2
import numpy as np
import matplotlib.pyplot as plt

def main():

	path = "C:\\Users\\spars\\OneDrive\\Pictures\\set\\"

	imgpath = path + "4.2.07.tiff"
	img = cv2.imread(imgpath, 0)

#	img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

	output1 = cv2.equalizeHist(img) 

	#clahe = cv2.createCLAHE()
	clahe = cv2.createCLAHE(clipLimit = 2.0, tileGridSize=(8,8))
	output2 = clahe.apply(img)

	output = [img,output1,output2]
	titles = ['Original Image', '', '']

	for i in range(3):
		plt.subplot(1,3,i+1)
		plt.imshow(output[i],cmap = 'gray')
		plt.title(titles[i])
		plt.xticks([])
		plt.yticks([])
	plt.show()

if __name__ == "__main__":
	main() 