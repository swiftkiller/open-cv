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

        output = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        cv2.imshow(windowName, frame)
        cv2.imshow('GRAY', output)
        if cv2.waitKey(1)==27:
            break

        
    cv2.destroyWindow(windowName)

    cap.release()

if __name__=="__main__":
    main()    

