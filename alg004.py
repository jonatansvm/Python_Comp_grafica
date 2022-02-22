"""Crie um algoritmo que altere a cor da imagem ‘olho.jpg’ para três formatos de cores que
auxiliem no processamento: Tons de Cinza, Lab e HSV. Mostre cada alteração de imagem em
uma janela diferente. Não é necessário salvar essas imagens."""

import cv2

imagem_ = cv2.imread("olho.jpg")

cinza = cv2.cvtColor(imagem_, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", cinza)
hsv = cv2.cvtColor(imagem_, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV", hsv)
lab_ = cv2.cvtColor(imagem_, cv2.COLOR_BGR2LAB)
cv2.imshow("LAB", lab_)

cv2.waitKey(0)
cv2.destroyAllWindows()
