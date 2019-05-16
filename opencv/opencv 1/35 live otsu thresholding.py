import cv2

def main():

    windowName='Live Video'
    cv2.namedWindow(windowName)
    cap=cv2.VideoCapture(0)
    if cap.isOpened():
        ret, frame = cap.read()  
    else:
        ret = False

    while ret:
        ret, frame = cap.read()

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        th = 0
        max_val = 255

        ret, o1 = cv2.threshold(frame, th, max_val, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        ret, o2 = cv2.threshold(frame, th, max_val, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
        ret, o3 = cv2.threshold(frame, th, max_val, cv2.THRESH_TOZERO + cv2.THRESH_OTSU)
        ret, o4 = cv2.threshold(frame, th, max_val, cv2.THRESH_TOZERO_INV + cv2.THRESH_OTSU)
        ret, o5 = cv2.threshold(frame, th, max_val, cv2.THRESH_TRUNC + cv2.THRESH_OTSU)

        	
        cv2.imshow(windowName, o1)
        if cv2.waitKey(1)==27:
            break

if __name__ == "__main__":
	main()
