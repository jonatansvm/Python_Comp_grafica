"""Aplique o Filtro Laplaciano para detecção de bordas e verifique o resultado. Analisar diversas
metodologias tem por finalidade comparar qual dos métodos melhor se adapta. Implemente
neste algoritmo o Laplaciano sobre a imagem em tons de cinza e após sobre ela equalizada"""

import numpy as np
import cv2

imagem_ = cv2.imread('olho.jpg')

imagem_ = cv2.cvtColor(imagem_, cv2.COLOR_BGR2GRAY)

lap = cv2.Laplacian(imagem_, cv2.CV_64F)
lap = np.uint8(np.absolute(lap))
resultado = np.vstack([imagem_, lap])
cv2.imshow("Laplaciano Simples", resultado)

his_eq = cv2.equalizeHist(imagem_)
lap_ = cv2.Laplacian(his_eq, cv2.CV_64F)
lap_ = np.uint8(np.absolute(lap_))
resultado_ = np.vstack([his_eq, lap_])
cv2.imshow("Laplaciano  Equa", resultado_)

cv2.waitKey(0)
cv2.destroyAllWindows()
