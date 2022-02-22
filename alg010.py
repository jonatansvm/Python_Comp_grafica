""" Outro fator importante para a construção de soluções de visão computacional é a detecção de
bordas, processo importantíssimo para localização de objetos, constatação de posição e
tamanho, entre outros. Sobre a imagem ‘olho.jpg’ aplique o método Sobel de detecção de
bordas. """

import numpy as np
import cv2

imagem_ = cv2.imread('olho.jpg')
imagem_ = cv2.cvtColor(imagem_, cv2.COLOR_BGR2GRAY)
sX = cv2.Sobel(imagem_, cv2.CV_64F, 1, 0)
sY = cv2.Sobel(imagem_, cv2.CV_64F, 0, 1)
sX = np.uint8(np.absolute(sX))
sY = np.uint8(np.absolute(sY))
sobel = cv2.bitwise_or(sX, sY)
resultado = np.vstack([np.hstack([imagem_, sX]), np.hstack([sY, sobel])])
cv2.imshow("SOBEL", resultado)

cv2.waitKey(0)
cv2.destroyAllWindows()
