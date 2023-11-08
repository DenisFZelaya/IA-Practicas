import cv2

im = cv2.imread("cat.jpg")
cv2.imshow("Original image",im)
cv2.imshow("Blurred Image", cv2.blur(im,(3,3)))
cv2.waitKey(0)
cv2.destroyAllWindows()
