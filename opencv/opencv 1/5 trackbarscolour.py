import cv2
import numpy as np

def empty():
    pass

def main():

    img=np.zeros((512,512,3),np.uint8)
    windowName='OpenCV bgr'
    cv2.namedWindow(windowName)

    cv2.createTrackbar('H', windowName, 0, 255, empty)    
    cv2.createTrackbar('S', windowName, 0, 255, empty)
    cv2.createTrackbar('V', windowName, 0, 255, empty)

    while(True):
        cv2.imshow(windowName, img)   

        if cv2.waitKey(1)==27:
            break
        blue = cv2.getTrackbarPos('B', windowName)
        red = cv2.getTrackbarPos('R', windowName)
        green = cv2.getTrackbarPos('G', windowName)
        
        img[:]=[blue,green,red]
        print(blue, red, green)

    cv2.destroyAllWindows()

if __name__== "__main__":
    main()
