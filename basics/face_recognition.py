import cv2
import dlib

#read the image
img=cv2.imread("all of dead.jpg")
#conver img to grayscale:3D->2D
gray=cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)
#dlib
face_detector=dlib.get_frontal_face_detector()
#use detector to find landmarks
faces=face_detector(gray)

for face in faces:
    x1=face.left()
    y1=face.top()
    x2=face.right()
    y2=face.bottom()
    #draw a rectangle
    cv2.rectangle(img=img,pt1=(x1,y1),pt2=(x2,y2), color=(0,255,0),thickness=3)
    break
#print(len(faces))
#show the image
cv2.imshow(winname="Face recoginition App ", mat=img)
#wait for a key press to exit
cv2.waitKey(delay=0)
#close All windows
cv2.destroyAllWindows()