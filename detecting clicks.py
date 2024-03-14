import cv2
import numpy as np

circles = np.zeros((4,2),np.int)
counter = 0
def mouse(events,x,y,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        circle[counter]=x,y
        counter=countr+1
        print(circles)

while True:
    if counter == 4 :
        img = cv2.imread("resources/img.png")
        width,height=250,350
        pts = np.float32([[267, 46], [424, 73], [230, 272], [390, 297]])
        pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
        matrix = cv2.getPerspectiveTransform(pts,pts2)
        output = cv2.warpPerspective(img,matrix,(width,height))

        cv2.circle(img,(267, 46), 1, (0, 0, 255))
        cv2.circle(img,(424, 73), 1, (0, 0, 255))
        cv2.circle(img,(230, 272), 1, (0, 0, 255))
        cv2.circle(img,(390, 297), 1, (0, 0, 255))
        cv2.imshow("output", output)

cv2.imshow("img",img)
cv2.setMouseCallback("output")
cv2.waitKey(0)
cv2.destroyAllWindows