"""Desenvolva um algoritmo para aumentar o contraste da imagem ‘olho.jpg’. Aplique a
transformação sobre a imagem em tons se cinza, com o objetivo de realçar os detalhes. Abaixo
a saída esperada do algoritmo."""
# aumentar o contraste da imagem ‘olho.jpg’

import cv2

imagem_ = cv2.imread("olho.jpg")

imagem_ = cv2.cvtColor(imagem_, cv2.COLOR_BGR2GRAY)
cv2.imshow("TONS DE CINZA", imagem_)

hist_eq = cv2.equalizeHist(imagem_)
cv2.imshow("IMAGEM MELHORADA", hist_eq)

cv2.waitKey(0)
cv2.destroyAllWindows()
