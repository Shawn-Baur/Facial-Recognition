import cv2, face_recognition, time

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

faces = []
allowedFaces = open("C:\\Users\\Freew\\OneDrive\\Desktop\\Python Projects\\OpenCV\\Face ID\\Allowed Faces", "r")
while(line := allowedFaces.readline().rstrip()):
    faces.append(line)

print(faces)

i = 0
img = []
for i in range(0, len(faces)):
    img.append(cv2.imread(faces[i]))
    #img.append(cv2.imread('ansh.jpg'))
    i = i + 1

i = 0
rgb_img = []
img_encoding = []
for i in range(0, len(img)):
    rgb_img.append(cv2.cvtColor(img[i], cv2.COLOR_BGR2RGB))
    img_encoding.append(face_recognition.face_encodings(rgb_img[i])[0])
    i = i + 1

#cv2.imshow('Pic of Shawn', img)

counter = 0
while (1):
    ok, frame = cap.read()
    
    if not ok:
        print('Error Reading Video')
        break
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face = face_cascade.detectMultiScale(gray, 1.1, 4)
    #time.sleep(1)
    #print(face)
    
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    for (x, y, w, h) in face:
        #if x>0 or y>0 or w>0 or h>0:
        try:
            frame_encoding = face_recognition.face_encodings(rgb_frame)[0]
        except IndexError as e:
            print('Error')
            break
        
        i = 0
        result = []
        for i in range(0, len(img_encoding)):
            result.extend(face_recognition.compare_faces([frame_encoding], img_encoding[i]))
            i = i + 1
            j = 0
            if True in result:
                print('Result: True')
        
        counter += 1
        break
        
    cv2.imshow('Frame', frame)
    
    key =cv2.waitKey(1)
    if key == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()