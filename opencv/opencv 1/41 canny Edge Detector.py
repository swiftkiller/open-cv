import cv2
import matplotlib.pyplot as plt
import numpy as np

def main():

	path = "C:\\Users\\spars\\OneDrive\\Pictures\\set\\"
	imgpath1 = path + '5.1.11.tiff'
	img = cv2.imread(imgpath1, 0)
	#img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

	L1 = cv2.Canny(img, 80, 180, L2gradient = False)
	L2 = cv2.Canny(img , 30, 100, L2gradient = True)

	titles=['original', 'L1', 'L2']
	outputs=[img, L1,L2]

	for i in range(3):
		plt.subplot(1,3,i+1)
		plt.imshow(outputs[i],cmap = 'gray')
		plt.title(titles[i])
	
	plt.show()

if __name__ == "__main__":
	main()		
