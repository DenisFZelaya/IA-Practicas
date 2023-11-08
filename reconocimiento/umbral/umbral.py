import cv2


# OPCIONES
# THRESH_BINARY
# THRESH_BINARY_INV
# THRESH_TRUNC
# THRESH_TOZERO
# THRESH_TOZERO_INV

img = cv2.imread("umbral-book.png")
retval, threshold = cv2.threshold(img, 62, 255, cv2.THRESH_BINARY)
# cv2.imshow("Original Image", img)
cv2.imshow("Threshold Image", threshold)
cv2.waitKey(0)
