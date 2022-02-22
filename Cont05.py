import cv2
import numpy as np

img = cv2.imread("futebol1.JPG")
#cv2.imshow("Dados", img)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
suave = cv2.GaussianBlur(gray,(7,7),0)
(T,bin) = cv2.threshold(suave, 160,255,cv2.THRESH_BINARY_INV)
#cv2.imshow("Bordar",bin)
_, objetos, _ = cv2.findContours(
    bin.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

contador = 0
for objeto in objetos:
    if len(objeto) > 60:
        contador += 1
        print("Objeto "+str(contador)+": ",len(objeto))
        cv2.drawContours(img, objeto, -1, (255,0,0),4)

cv2.imshow("Bordar",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
