import numpy as np
import matplotlib.pyplot as plt
import cv2

imagen = cv2.imread('00_Ficheros/cara.jpg')

imagen = cv2.blur(imagen, ksize=(5,5))

contorno = cv2.Canny(image=imagen, threshold1=100, threshold2=100)




plt.imshow(contorno)
plt.show()