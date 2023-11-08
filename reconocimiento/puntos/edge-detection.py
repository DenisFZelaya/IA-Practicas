import cv2

img = cv2.imread("cat.jpg")
edges = cv2.Canny(img, 250, 200)

cv2.imshow("CAT", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()