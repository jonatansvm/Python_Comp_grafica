"""Crie um algoritmo para recortar as posições Eixo X (de 250 até 540) e Eixo Y (de 60 até 220) e
salvar essa fração de imagem com o nome ‘olho.jpg’. Abaixo a resposta do processamento."""

#recortar as posições Eixo X (de 250 até 540)
#salvar essa fração de imagem com o nome ‘olho.jpg’

import cv2

imagem_ = cv2.imread("olhoazul.jpg")
crop_imagem_ = imagem_[60:220,250:540]
cv2.imwrite('olho.jpg',crop_imagem_)


cv2.waitKey(0)
cv2.destroyAllWindows()

