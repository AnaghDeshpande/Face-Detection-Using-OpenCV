import cv2
frameWidth = 0
frameHeight = 0
cap = cv2.VideoCapture(0)
cap.set(8,frameWidth)
cap.set(4,frameHeight)
while True:
    success,vid=cap.read()
    cv2.imshow("video",vid)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cap.release()
cv2.destroyALlWindows()