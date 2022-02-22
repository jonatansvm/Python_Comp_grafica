"""Sabemos que a binarização de uma imagem com limiarização depende de um valor de
referência, que muitas vezes é variável de acordo com a luminosidade e qualidade da imagem.
Para tanto, crie um algoritmo que aplique Threshold Adaptativo sobre a imagem do ‘olho.jpg’
gerando a binarização com base nas características da imagem. """
# algoritmo que aplique Threshold Adaptativo sobre a imagem do ‘olho.jpg’
# gerando a binarização com base nas características da imagem.

import cv2
import numpy as np

imagem_ = cv2.imread('olho.jpg')
imagem_ = cv2.cvtColor(imagem_, cv2.COLOR_BGR2GRAY)
suave = cv2.GaussianBlur(imagem_, (7, 7), 0)
bin1 = cv2.adaptiveThreshold(suave, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 21, 5)
bin2 = cv2.adaptiveThreshold(suave, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 21, 5)
resultado = np.vstack([np.hstack([imagem_, suave]), np.hstack([bin1, bin2])])
cv2.imshow("BINARIZACAO ADAPTATIVA DA IMAGEM", resultado)

cv2.waitKey(0)
cv2.destroyAllWindows()
