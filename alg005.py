"""Crie um código para plotar na tela um histograma da imagem ‘olho.jpg’ em tons de cinza. É
possível perceber que existe um grande número de pixels com intensidade entre 170 e 230 de
cor que indicam cores mais claras (Branco = 255 , Preto = 0)."""

import cv2
from matplotlib import pyplot as plt

imagem_ = cv2.imread("olho.jpg")
imagem_ = cv2.cvtColor(imagem_, cv2.COLOR_BGR2GRAY)

plt.title("Histograma TONS DE CINZA")
plt.xlabel("Intensidade")
plt.ylabel("Quantidade de Pixels")
plt.hist(imagem_.ravel(), 256, [0, 256])
plt.xlim([0, 256])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
