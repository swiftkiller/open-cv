import cv2

def emptyfunction():
	pass

def main():

	path = "C:\\Users\\spars\\OneDrive\\Pictures\\Camera Roll\\"

	imgpath1= path + "WIN_20170902_18_09_13_Pro.jpg"
	imgpath2= path + "WIN_20190301_18_04_19_Pro.jpg"
	
	img1 = cv2.imread(imgpath1, 1)
	img2 = cv2.imread(imgpath2, 1)

	output=cv2.addWeighted(img1, 0.5, img2, 0.5,0)

	windowName= 'Transition Demo'
	cv2.namedWindow(windowName)

	cv2.createTrackbar('Alpha', windowName,0,100,emptyfunction)

	while(True):
		cv2.imshow(windowName, output)

		if cv2.waitKey(1)==27:
			break

		alpha = cv2.getTrackbarPos('Alpha', windowName)/100
		beta = 1-alpha

		output = cv2.addWeighted(img1,alpha,img2,beta,0)	

		print(alpha,beta) 

	cv2.destroyAllWindows()
	
if __name__ == '__main__':
	main()			