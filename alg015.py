"""Baseado no exercício anterior, implemente um algoritmo que detecte somente a pupila e
indique a posição no eixo X e no eixo Y da mesma. Como demostrado no exemplo abaixo:
"""

import cv2
import numpy as np

while (1):
    imagem_ = cv2.imread('olho.jpg')
    hsv = cv2.cvtColor(imagem_, cv2.COLOR_BGR2HSV)
    black_lower = np.array([0, 0, 0], np.uint16)
    black_upper = np.array([180, 255, 40], np.uint16)
    black = cv2.inRange(hsv, black_lower, black_upper)
    kernel = np.ones((5, 5), "uint8")
    black = cv2.morphologyEx(black, cv2.MORPH_OPEN, kernel)
    black = cv2.morphologyEx(black, cv2.MORPH_CLOSE, kernel)
    black = cv2.erode(black, kernel, iterations=1)
    res1 = cv2.bitwise_and(imagem_, imagem_, mask=black)
    (_, contours, hierarchy) = cv2.findContours(black, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        mayor_contorno = max(contours, key=cv2.contourArea)

        if (area > 120):
            x, y, w, h = cv2.boundingRect(contour)
            imagem_ = cv2.rectangle(imagem_, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.putText(imagem_, "X:{}Y:{}".format(x, y), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0))

    cv2.imshow("RESULTADO FINAL:", imagem_)
    if cv2.waitKey(10) & 0xFF == 27:
        cv2.destroyAllWindows()
        break
