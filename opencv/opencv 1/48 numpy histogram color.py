import cv2
import numpy as np
import matplotlib.pyplot as plt

def main():

	path = "C:\\Users\\spars\\OneDrive\\Pictures\\set\\"

	imgpath = path + "4.2.07.tiff"
	img = cv2.imread(imgpath, 1)
	img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

	r,g,b=cv2.split(img)

	plt.subplot(2, 2, 1)
	plt.imshow(img, cmap= 'gray')
	plt.title('Image')
	plt.xticks([])
	plt.yticks([])

	plt.subplot(2, 2, 2)
	hist, bins = np.histogram(r.ravel(),256,[0,255])
	plt.title('r histogram')
	plt.xlim([0,255])
	plt.ylim([0,5000])
	plt.plot(hist,color='r')

	plt.subplot(2, 2, 3)
	hist, bins = np.histogram(g.ravel(),256,[0,255])
	plt.title('g histogram')
	plt.xlim([0,255])
	plt.ylim([0,5000])
	plt.plot(hist,color = 'g')

	plt.subplot(2, 2, 4)
	hist, bins = np.histogram(b.ravel(),256,[0,255])
	plt.title('b histogram')
	plt.xlim([0,255])
	plt.ylim([0,5000])
	plt.plot(hist,color= 'b')

	plt.show()

if __name__ == "__main__":
	main() 
