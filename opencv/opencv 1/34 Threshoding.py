import cv2

def main():

    windowName='Live Video'
    cv2.namedWindow(windowName)
    cap=cv2.VideoCapture(0)
    if cap.isOpened():
        ret, frame = cap.read()
        print(frame)   
    else:
        ret = False

    while ret:
        ret, frame = cap.read()

        th = 130
        max_val = 255

        ret, o1 = cv2.threshold(frame, th, max_val, cv2.THRESH_BINARY)
        ret, o2 = cv2.threshold(frame, th, max_val, cv2.THRESH_BINARY_INV)
        ret, o3 = cv2.threshold(frame, th, max_val, cv2.THRESH_TOZERO)
        ret, o4 = cv2.threshold(frame, th, max_val, cv2.THRESH_TOZERO_INV)
        ret, o5 = cv2.threshold(frame, th, max_val, cv2.THRESH_TRUNC)
        	
        cv2.imshow(windowName, o2)
        if cv2.waitKey(1)==27:
            break

if __name__ == "__main__":
	main()
