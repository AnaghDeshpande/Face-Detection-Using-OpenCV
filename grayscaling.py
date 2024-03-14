# 3 ways of grayscaling
# 1.  cvtColor
# 2. flag = 0 in imread
# 3. pixel manipulation

import cv2
img = cv2.imread("resources/image.png")
cv2.imshow("photo",img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("grayscale",gray)

blur = cv2.GaussianBlur(img,(7,7),0)   #blurring the image
cv2.imshow("blurred image",blur)

canny = cv2.Canny(img,100,100) #edge detection.
# further image functions like erode and dilation can be used to decrease or increase the thickness of the edge lines
cv2.imshow("canny", canny)

cv2.waitKey(0)
cv2.destroyAllWindows()