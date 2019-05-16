import cv2
import numpy as np
import matplotlib.pyplot as plt

def main():

	path = "C:\\Users\\spars\\OneDrive\\Pictures\\set\\"

	imgpath = path + "4.2.06.tiff"
	img = cv2.imread(imgpath, 1)
	img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

	r,g,b = cv2.split(img)


	output1_r = cv2.equalizeHist(r) 
	output1_g = cv2.equalizeHist(g)
	output1_b = cv2.equalizeHist(b)

	output1 = cv2.merge((output1_r,output1_b,output1_g))

	#clahe = cv2.createCLAHE()
	clahe = cv2.createCLAHE(clipLimit = 2.0, tileGridSize=(8,8))
	output2_r = clahe.apply(r)
	output2_g = clahe.apply(g)
	output2_b = clahe.apply(b)

	output2 = cv2.merge((output2_r,output2_b,output2_g))

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