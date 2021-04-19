import cv2 as cv

cap = cv.VideoCapture(0)

haar_cascade = cv.CascadeClassifier('haar_face.xml')

neigh=3

def changeNeigh(newN):
    global neigh
    neigh = newN
    print(f'Current minNeighbours: {neigh}')

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret:
        gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
        faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=neigh)

        for(x,y,w,h) in faces_rect:
            cv.rectangle(frame,(x,y),(x+w,y+h), (0,255,0),thickness=2)

        cv.imshow('frame',frame)

        k = cv.waitKey(1)

        if k == ord('q'):
            break
        elif k == ord('+'):
            changeNeigh(neigh+1)
        elif k == ord('-'):
            changeNeigh(neigh-1)

    else:
        break

cap.release()
cv2.destroyAllWindows()