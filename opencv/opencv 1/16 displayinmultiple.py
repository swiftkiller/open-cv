import cv2
import matplotlib.pyplot as plt

def main():

	path = "C:\\Users\\spars\\OneDrive\\Pictures\\Camera Roll\\"

	imgpath1=path+"WIN_20170902_18_09_13_Pro.jpg"
	imgpath2= path + "pika.jpg"
	
	img1 = cv2.imread(imgpath1, 1)
	img2 = cv2.imread(imgpath2, 1)

	img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
	img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

	titles = ['Gyo', 'snoker']
	images = [img1, img2] 

	for i in range(2):
		plt.subplot(1, 2, i+1)
		plt.imshow(images[i])
		plt.title(titles[i])
		plt.xticks([])
		plt.yticks([])
	plt.show()

if __name__ == "__main__":
	main()
