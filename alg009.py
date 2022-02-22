import mahotas
import numpy as np
import cv2

imagem_ = cv2.imread('olho.jpg')
imagem_ = cv2.cvtColor(imagem_, cv2.COLOR_BGR2GRAY)
suave = cv2.GaussianBlur(imagem_, (7, 7), 0)
T = mahotas.thresholding.otsu(suave)
temp = imagem_.copy()
temp[temp > T] = 255
temp[temp < 255] = 0
temp = cv2.bitwise_not(temp)
T = mahotas.thresholding.rc(suave)
temp2 = imagem_.copy()
temp2[temp2 > T] = 255
temp2[temp2 < 255] = 0
temp2 = cv2.bitwise_not(temp2)
resultado = np.vstack([np.hstack([imagem_, suave]), np.hstack([temp, temp2])])
cv2.imshow("BINARIZACAO COM METODO OTSU E RIDDLER-CALVARD", resultado)

cv2.waitKey(0)
cv2.destroyAllWindows()
