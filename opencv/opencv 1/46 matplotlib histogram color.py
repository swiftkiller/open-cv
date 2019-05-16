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
	plt.imshow(img)
	plt.title('Image')
	plt.xticks([])
	plt.yticks([])

	plt.subplot(2, 2, 2)
	plt.hist(r.ravel(), 256 ,[0,255])
	plt.title('red histogram')
	plt.xlim(xmin=0,xmax=256)

	plt.subplot(2, 2, 3)
	plt.hist(b.ravel(), 256 ,[0,255])
	plt.title('blue histogram')
	plt.xlim(xmin=0,xmax=256)

	plt.subplot(2, 2, 4)
	plt.hist(g.ravel(), 256 ,[0,255])
	plt.title('green histogram')
	plt.xlim(xmin=0,xmax=256)

	plt.show()

if __name__ == "__main__":
	main() 
