import cv2
import numpy as np
img = cv2.imread("resources/img.png")


width,height=250,350
pts = np.float32([[267, 46], [424, 73], [230, 272], [390, 297]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts,pts2)
output = cv2.warpPerspective(img,matrix,(width,height))

cv2.circle(img,(int(pts[0][0]),int(pts[0][1])), 1, (0, 0, 255))

# cv2.circle(img,(424, 73), 1, (0, 0, 255))
# cv2.circle(img,(230, 272), 1, (0, 0, 255))
# cv2.circle(img,(390, 297), 1, (0, 0, 255))
cv2.imshow("img",img)
cv2.imshow("output",output)
cv2.waitKey(0)
cv2.destroyAllWindows()