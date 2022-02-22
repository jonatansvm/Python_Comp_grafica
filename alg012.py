"""Analisando mais um método de detecção de bordas, aplique sobre o olho o detector Canny.
Utilize como referência os parâmetros 100 e 300 para obter o seguinte resultado."""

import numpy as np
import cv2

imagem_ = cv2.imread('olho.jpg')

suave = cv2.GaussianBlur(imagem_, (7, 7), 0)
canny1 = cv2.Canny(suave, 100, 300)

result = np.hstack([canny1])
cv2.imshow("DETECTOR DE BORDAS CANNY", result)

cv2.waitKey(0)
cv2.destroyAllWindows()

