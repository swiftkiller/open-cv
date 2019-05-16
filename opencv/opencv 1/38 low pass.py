import cv2
import matplotlib.pyplot as plt
import numpy as np

def main():

	path = "C:\\Users\\spars\\OneDrive\\Pictures\\set\\"
	imgpath1 = path + '4.2.07.tiff'
	img = cv2.imread(imgpath1, 1)
	img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

	box = cv2.boxFilter(img,-1,(53,53))
	blur = cv2.blur(img,(13,13))
	Gaussian = cv2.GaussianBlur(img,(27,27),0)

	titles=['original', 'box', 'blur', 'Gaussian']
	outputs=[img, box, blur,Gaussian]

	for i in range(4):
		plt.subplot(2,2,i+1)
		plt.imshow(outputs[i])
		plt.title(titles[i])
	
	plt.show()

if __name__ == "__main__":
	main()		
