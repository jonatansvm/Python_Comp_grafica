"""Implemente um algoritmo para detectar somente a cor azul na imagem ‘olho.jpg’. Utilize o
sistema de cores HSV e aplique a seguinte máscara para filtrar o range.
a. lower_blue = np.array([90,50,38]) e upper_blue = np.array([130,255,255]).
b. Mostre na tela a imagem original, a máscara e o resultado, como o exemplo abaixo:"""

import numpy as np
import cv2

while (1):
    frame = cv2.imread('olho.jpg')
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([90, 50, 38])
    upper_blue = np.array([130, 255, 255])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    res = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow('Mascara', mask)
    cv2.imshow('Resultado', res)
    cv2.imshow('Imagem', frame)
    k = cv2.waitKey(5) & 0xFF

    if k == 27:
        break

cv2.waitKey(0)
cv2.destroyAllWindows()
