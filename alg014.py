"""Aplicando técnicas de morphologyEx, melhore a imagem binária, retirando pixels ‘solitários’ e
completando falhas em linhas continuas (cv2.MORPH_OPEN e cv2.MORPH_CLOSE). Após
identifique a córnea e trace um retângulo em sua volta com o tamanho em pixels, como o
exemplo abaixo:"""

import cv2
import numpy as np

while (1):
    imagem_ = cv2.imread('olho.jpg')
    hsv = cv2.cvtColor(imagem_, cv2.COLOR_BGR2HSV)
    blue_lower = np.array([90, 50, 38], np.uint8)
    blue_upper = np.array([130, 255, 255], np.uint8)
    blue = cv2.inRange(hsv, blue_lower, blue_upper)
    kernel = np.ones((5, 5), "uint8")
    blue = cv2.morphologyEx(blue, cv2.MORPH_OPEN, kernel)
    blue = cv2.morphologyEx(blue, cv2.MORPH_CLOSE, kernel)
    blue = cv2.erode(blue, kernel, iterations=1)
    res1 = cv2.bitwise_and(imagem_, imagem_, mask=blue)
    (_, contours, hierarchy) = cv2.findContours(blue, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        mayor_contorno = max(contours, key=cv2.contourArea)
        if (area > 2000):
            x, y, w, h = cv2.boundingRect(contour)
            imagem_ = cv2.rectangle(imagem_, (x, y), (x + w, y + h), (255, 0, 0), 1)
            cv2.putText(imagem_, "W:{}H:{}".format(x, y), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 1)
    cv2.imshow("RESULTADO: ", imagem_)

    if cv2.waitKey(10) & 0xFF == 27:
        cv2.destroyAllWindows()
        break
