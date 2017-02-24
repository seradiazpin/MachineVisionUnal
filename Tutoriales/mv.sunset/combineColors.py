import colort_utils as cu
import cv2

targetColors = cv2.imread("../mv.images/reglamen.jpg")
normal = cv2.imread("../mv.images/Rojos.png")


transfer = cu.color_transfer(normal,targetColors)

cv2.imshow("targer",targetColors)
cv2.imshow("tNormal",normal)
cv2.imshow("color",transfer)
cv2.waitKey(0)