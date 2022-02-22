import cv2

imagem_ = cv2.imread("olhoazul.jpg")
cv2.imshow("Olhos azuis", imagem_)

cv2.waitKey(0)
cv2.destroyAllWindows()
