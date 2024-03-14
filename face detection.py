import cv2
face=cv2.CascadeClassifier("resources\haarcascade_frontalface_default.xml")
im=cv2.VideoCapture(0)
while True:
    ret,frame = im.read()
    # cv2.imshow("frame",frame)
    faces = face.detectMultiScale(frame, minSize=(25, 25), scaleFactor=1.1, minNeighbors=5,flags=cv2.CASCADE_SCALE_IMAGE)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + y, y + h), (0, 255, 0), 2)

    cv2.imshow("frame",frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cv2.waitKey(0)
im.release()
cv2.destroyAllWindows()