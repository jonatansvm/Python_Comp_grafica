"""

AZUL = move cursor
AMARELO = clique esquerdo
VERDE CLARO = clique direito
LARANJA = digita ESC fechando tudo

todos foram testados
"""

import cv2
import numpy as np
import pyautogui

cap = cv2.VideoCapture(0)
D = []
max_samples = 10000

while (1):
    d = 0.1
    centers = []
    _, imagem_ = cap.read()
    hsv = cv2.cvtColor(imagem_, cv2.COLOR_BGR2HSV)
    blue_lower = np.array([95, 150, 100], np.uint8)
    blue_upper = np.array([150, 255, 255], np.uint8)
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

        if (area > 1000):
            x, y, w, h = cv2.boundingRect(contour)
            imagem_ = cv2.rectangle(imagem_, (x, y), (x + w, y + h), (255, 0, 0), 2)
            pyautogui.moveTo(x + w, y + h)
    # LEFT MOUSE
    yellow_lower = np.array([90, 50, 38], np.uint8)
    yellow_upper = np.array([130, 255, 255], np.uint8)
    yellow = cv2.inRange(hsv, yellow_lower, yellow_upper)
    kernel = np.ones((5, 5), "uint8")
    yellow = cv2.morphologyEx(yellow, cv2.MORPH_OPEN, kernel)
    yellow = cv2.morphologyEx(yellow, cv2.MORPH_CLOSE, kernel)
    yellow = cv2.erode(yellow, kernel, iterations=1)
    res1 = cv2.bitwise_and(imagem_, imagem_, mask=yellow)

    (_, contours, hierarchy) = cv2.findContours(yellow, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        mayor_contorno = max(contours, key=cv2.contourArea)

        if (area > 1000):
            x, y, w, h = cv2.boundingRect(contour)
            imagem_ = cv2.rectangle(imagem_, (x, y), (x + w, y + h), (255, 255, 0), 2)
            pyautogui.click()

    # RIGHT MOUSE
    green_lower = np.array([45, 59, 119], np.uint8)
    green_upper = np.array([68, 255, 255], np.uint8)
    green = cv2.inRange(hsv, green_lower, green_upper)
    kernel = np.ones((5, 5), "uint8")
    green = cv2.morphologyEx(green, cv2.MORPH_OPEN, kernel)
    green = cv2.morphologyEx(green, cv2.MORPH_CLOSE, kernel)
    green = cv2.erode(green, kernel, iterations=1)
    res1 = cv2.bitwise_and(imagem_, imagem_, mask=green)
    (_, contours, hierarchy) = cv2.findContours(green, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        mayor_contorno = max(contours, key=cv2.contourArea)

        if (area > 2000):
            x, y, w, h = cv2.boundingRect(contour)
            imagem_ = cv2.rectangle(imagem_, (x, y), (x + w, y + h), (0, 255, 0), 2)
            pyautogui.rightClick()

    #FECHA O SISTEMA PRECIONANDO "ESC"
    orange_lower = np.array([15, 30, 60], np.uint8)
    orange_upper = np.array([15, 255, 255], np.uint8)
    orange = cv2.inRange(hsv, orange_lower, orange_upper)
    kernel = np.ones((5, 5), "uint8")
    orange = cv2.morphologyEx(orange, cv2.MORPH_OPEN, kernel)
    orange = cv2.morphologyEx(orange, cv2.MORPH_CLOSE, kernel)
    orange = cv2.erode(orange, kernel, iterations=1)
    res1 = cv2.bitwise_and(imagem_, imagem_, mask=orange)
    (_, contours, hierarchy) = cv2.findContours(orange, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        mayor_contorno = max(contours, key=cv2.contourArea)

        if (area > 1000):
            x, y, w, h = cv2.boundingRect(contour)
            imagem_ = cv2.rectangle(imagem_, (x, y), (x + w, y + h), (135, 31, 120), 2)
            pyautogui.press("esc")
    cv2.imshow("CARREGANDO COR:", imagem_)

    if cv2.waitKey(10) & 0xFF == 27:
        break

cv2.destroyAllWindows()
