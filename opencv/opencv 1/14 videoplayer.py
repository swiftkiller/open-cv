import cv2

def main():
    windowName='Video PLAYER'
    cv2.namedWindow(windowName)
    filename = 'C:\\Users\\spars\\Desktop\\programs\\python\\opencv\\output\\lfr.avi'
    cap=cv2.VideoCapture(filename)        

    while (cap.isOpened()):

        ret, frame = cap.read()
        print(ret)

        #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        if ret:
            cv2.imshow(windowName, frame)
            if cv2.waitKey(33)==27:
                break
        else:
            break

        
    cv2.destroyAllWindows()
    cap.release()
if __name__=="__main__":
    main()    
