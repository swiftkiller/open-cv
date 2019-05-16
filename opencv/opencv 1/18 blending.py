import cv2
import matplotlib.pyplot as plt

def main():

	path = "C:\\Users\\spars\\OneDrive\\Pictures\\Camera Roll\\"

	imgpath1= path + "WIN_20170902_18_09_13_Pro.jpg"
	imgpath2= path + "WIN_20190301_18_04_19_Pro.jpg"
	
	img1 = cv2.imread(imgpath1, 1)
	img2 = cv2.imread(imgpath2, 1)

	img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
	img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
	
	alpha = 0.3
	beta = 0.7
	gamma = 0

	output=cv2.addWeighted(img1, alpha, img2, beta,gamma)
	add = img1 + img2

	titles = ['Gyo', 'snoker', 'Blended', 'Add']
	images = [img1, img2, output, add] 

	for i in range(4):
		plt.subplot(1, 4, i+1)
		plt.imshow(images[i])
		plt.title(titles[i])
		plt.xticks([])
		plt.yticks([])
	plt.show()

if __name__ == '__main__':
	main()
