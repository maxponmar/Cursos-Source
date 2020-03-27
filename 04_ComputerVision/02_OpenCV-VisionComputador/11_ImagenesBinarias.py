import matplotlib.pyplot as plt
import cv2

imagen = cv2.imread('00_Ficheros/perro.jpg', 0)

mitad, imagen =  cv2.threshold(imagen, 255/2,255, cv2.THRESH_BINARY)
plt.imshow(imagen, cmap='gray')
plt.show()