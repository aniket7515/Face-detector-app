import cv2
#Loading of some pretrained data for open cv (haarascsde )
trained_face_data=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#Choose image to detect faces

#img=cv2.imread('RT.jpg')

#TO CAPTURE THE VIDEO FROM WEBCAM
webcam=cv2.VideoCapture(0)
# iterate forever over frames
while True:
    # Read the current frames
    successful_frame_read,frame=webcam.read()
    #must convert to gray scale
    grayscaled_img=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #Detect faces
    face_coordinates=trained_face_data.detectMultiScale(grayscaled_img)
    #Draw rectangle around the faces
    for (x,y,w,h) in face_coordinates:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)


    cv2.imshow('Aniket Dhokane face detection ',frame)
    cv2.waitKey(1)

#Must convert to gray scale the image

#grayscaled_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# Detect Faces
#face_coordinates=trained_face_data.detectMultiScale(grayscaled_img)
# Draw rectangles around the faces
#for (x,y,w,h) in face_coordinates:
#(x,y,w,h)=face_coordinates[0]
#    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)


#print(face_coordinates)

#DISPLAY THE IMAGES WITH FACES
#cv2.imshow('Aniket Dhokane face detector ',img)
#cv2.waitKey()
print("Code complete")