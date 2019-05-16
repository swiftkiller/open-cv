import cv2
import numpy as np
import matplotlib.pyplot as plt

def main():

	path = "C:\\Users\\spars\\OneDrive\\Pictures\\set\\"

	imgpath = path + "4.2.07.tiff"
	img = cv2.imread(imgpath, 1)
	img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

	red_hist = cv2.calcHist([img], [0], None, [256],[0,255])
	green_hist = cv2.calcHist([img], [1], None, [256],[0,255])
	blue_hist = cv2.calcHist([img], [2], None, [256],[0,255])

	plt.subplot(4, 1, 1)
	plt.imshow(img)
	plt.title('Image')
	plt.xticks([])
	plt.yticks([])

	plt.subplot(4,1, 2)
	plt.title('r histogram')
	plt.xlim([0,255])
	plt.ylim([0,5000])
	plt.plot(red_hist,color='r')

	plt.subplot(4, 1, 3)
	plt.title('g histogram')
	plt.xlim([0,255])
	plt.ylim([0,5000])
	plt.plot(green_hist,color = 'g')

	plt.subplot(4, 1, 4)
	plt.title('b histogram')
	plt.xlim([0,255])
	plt.ylim([0,5000])
	plt.plot(blue_hist,color= 'b')

	plt.show()

if __name__ == "__main__":
	main() 