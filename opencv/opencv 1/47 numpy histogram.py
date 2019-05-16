import cv2
import numpy as np
import matplotlib.pyplot as plt

def main():

	path = "C:\\Users\\spars\\OneDrive\\Pictures\\set\\"

	imgpath = path + "4.2.07.tiff"
	img = cv2.imread(imgpath, 0)

	plt.subplot(1, 2, 1)
	plt.imshow(img, cmap= 'gray')
	plt.title('Image')
	plt.xticks([])
	plt.yticks([])

	plt.subplot(1, 2, 2)
	hist, bins = np.histogram(img.ravel(),256,[0,255])
	plt.title('histogram')
	plt.xlim([0,255])
	plt.ylim([0,3000])
	plt.plot(hist)
	plt.show()

if __name__ == "__main__":
	main() 
