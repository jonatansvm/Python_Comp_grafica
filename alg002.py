"""Aperfeiçoe seu algoritmo, pegando a informação da cor do pixel x= 400 e y = 160 (BGR) e
mostrando na tela ao executar o code. Aplique neste mesmo código a coleta de resolução da
imagem, mostrando no prompt as informações de altura, largura e profundidade. Abaixo a
resposta que deve ser mostrado:"""

# cor do pixel x= 400 e y = 160
# resolução da imagem
# mostrando no prompt as informações de altura, largura e profundidade

import cv2
import numpy as np

imagem_ = cv2.imread("olhoazul.jpg")
h, w, bpp = np.shape(imagem_)
print("Altura:", h)
print("Largura:", w)
print("Profundidade:", bpp)

(b, g, r) = imagem_[160, 400]
print("Cor do pixel em (160, 400) - Vermelho: {}, Verde: {}, Azul: {}".format(r, g, b))

cv2.waitKey(0)
cv2.destroyAllWindows()
