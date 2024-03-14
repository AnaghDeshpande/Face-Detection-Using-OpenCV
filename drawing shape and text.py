import cv2
import numpy as np
U1 = np.zeros((512,512))#it creates a matrix of 512x512
img = np.zeros((512,512,3),np.uint8) # we add 3 in order to create the channel (BGR). the point after the 0 in the matrix
# represents that it can store float values also. but for colors we use int so we change it to int by using unsigned 8 bit int(uint8)
cv2.imshow("img",img)
img[:]=255,0,0
print(U1)
print(img)
cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# import cv2
# import numpy as np
# img=np.zeros((512,512,3),np.uint8)
# cv2.line(img,(0,0),(100,250),(255,0,0),2)#syntax = cv2.line(image name, origin, end, color, thickness)
# #for a full diagonal replace (100,100) by (img.shape[1],img.shape[0])
# cv2.rectangle(img,(213,5),(99,99),(0,0,135),cv2.FILLED)#syntax is same as line's
# cv2.circle(img,(213,245),99,(0,0,135),6)
# cv2.putText(img,"i am anagh",(48,394),cv2.FONT_ITALIC,2,(178,128,0),3)#2 represents the scale
# print(img)
#
# cv2.imshow("img",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows