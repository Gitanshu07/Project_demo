import cv2
import numpy as np

face_classifier = cv2.CascadeClassifier('C:/Users/Gitanshu/Anaconda3/Lib/site-packages/cv2/data/haarcascade_frontalcatface_default.xml')

def face_extractor(img): 
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cap = cv2.VideoCapture(0)
count = 0

while True:
    ret,frame = cap.read()
    
    if face_extractor(frame) is not None:
        count += 1
        
        face = cv2.resize(face_extractor(frame),(200,200))
        face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
        
        file_name_path = 'C:/Users/Gitanshu/Untitled Folder/sample_images/user'+str(count) + '.jpg'
        cv2.imwrite(file_name_path,face)
        
        cv2.putText(face,str(count),(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
        
        cv2.imshow('FACE CROPPER',face)
        
    else:
        print("Face Not Found")
        pass
    
    if cv2.waitKey(1) == 27 or count == 100:
        break

cap.release()
cv2.destroyAllWindows()
print("Collecting Samples Complete!!!")
