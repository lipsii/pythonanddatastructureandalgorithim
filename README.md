# pythonanddatastructureandalgorithim
pythonanddatastructure 
import cv2
casecade_face =cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
while True:
    ret,img = cap.read()
    print(ret)
    g = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    f = casecade_face.detectMultiScale(g,1.3,4)
    
    
    for (x,y,w,h) in f:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),4)
        
    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break 
        
cap.release()
cv2.destroyAllWindows()        
