"""Altere o código para plotar na tela o histograma colorido, das cores Azul, Vermelho e Verde da
imagem original ‘olho.jpg’."""

import cv2
from matplotlib import pyplot as plt

imagem_ = cv2.imread("olho.jpg")

canais = cv2.split(imagem_)
cores = ("b", "g", "r")
plt.figure()
plt.title("'Histograma COLORIDO")
plt.xlabel("Intensidade")
plt.ylabel("Número de Pixels")
corindice = 0
for canal in canais:
    hist = cv2.calcHist([canal], [0], None, [256], [0, 256])
    plt.plot(hist, cores[corindice])
    corindice = corindice + 1
    plt.xlim([0, 256])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
