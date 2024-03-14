import cv2
img = cv2.imread("resources/image.png")
# print(img)#prints the intensities of the rgb
# print(img.shape) #prints the siz of the image  shape syntax- (height,width,channel)
#
# resize = cv2.resize(img,(900,700))#syntax is (image variable,(width,height)) nut in output it shows height,width,channel
cv2.imshow("image",img)
# cv2.imshow("resized image",resize)
# print(resize.shape)

#cropping an image
crop1 = img[50:100,0:100]
crop2 = img[0:100,50:100]#syntax of img[height,width]
cv2.imshow("crop1",crop1)
cv2.imshow("crop2",crop2)

# it makes the size of the selected image same as the size of the original image
imgcropresize1 = cv2.resize(crop2,(img.shape[0],img.shape[1])) #rsize(imagename,(width,height)) 0 and 1 values are used in case if
# we dont know the original dimension of the image *in other words it scales the chosen(crop2) image to the dimension of the original image(img)
imgcropresize2 = cv2.resize(crop2,(img.shape[1],img.shape[0]))#why 0 and 1 only why not 0,0 1,1 or 1,0 ???
cv2.imshow("imgcropresize1",imgcropresize1)
cv2.imshow("imgcropresize2",imgcropresize2)

cv2.waitKey(0)
cv2.destroyAllWindows