import cv2
import numpy as np
import matplotlib.pyplot as plt

def main():

	path = "C:\\Users\\spars\\OneDrive\\Pictures\\set\\"

	imgpath = path + "4.2.07.tiff"
	img = cv2.imread(imgpath, 1)
	img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

	z = img.reshape((-1,1))
	z = np.float32(z)

	creteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER,10,1.0)

	k = 3
	ret, label1,center1 = cv2.kmeans(z,k,None,creteria,10,cv2.KMEANS_RANDOM_CENTERS)
	center1 = np.uint8(center1)
	res1 = center1[label1.flatten()]
	output1 =  res1.reshape((img.shape))

	k = 6
	ret, label1,center1 = cv2.kmeans(z,k,None,creteria,10,cv2.KMEANS_RANDOM_CENTERS)
	center1 = np.uint8(center1)
	res1 = center1[label1.flatten()]
	output2 =  res1.reshape((img.shape))

	k = 9 
	ret, label1,center1 = cv2.kmeans(z,k,None,creteria,10,cv2.KMEANS_RANDOM_CENTERS)
	center1 = np.uint8(center1)
	res1 = center1[label1.flatten()]
	output3 =  res1.reshape((img.shape))


	output = [img, output1, output2, output3]
	titles = ['Image', 'k=2', 'k=4','k=6']

	for i in range(4):
		plt.subplot(2, 2, i+1)
		plt.imshow(output[i])
		plt.title(titles[i])
		plt.xticks([])
		plt.yticks([])
	plt.show()

if __name__ == "__main__":
	main() 