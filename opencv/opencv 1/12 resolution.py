import cv2

def main():
    windowName='Live Video'
    cv2.namedWindow(windowName)
    cap=cv2.VideoCapture(0)

    print('Width : ' + str(cap.get(3)))
    print('Height : ' + str(cap.get(4)))

    cap.set(3,1024)
    cap.set(4, 768)

    print('Width : ' + str(cap.get(3)))
    print('Height : ' + str(cap.get(4)))
    
    if cap.isOpened():
        ret, frame = cap.read()
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
    cv2.destroyWindow(output)
    
    cap.release()

if __name__=="__main__":
    main()    
a
