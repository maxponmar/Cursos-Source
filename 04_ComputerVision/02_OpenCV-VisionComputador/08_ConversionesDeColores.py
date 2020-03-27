import matplotlib.pyplot as plt
import cv2

imagen = cv2.imread('00_Ficheros/perro.jpg')

imagen2 = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)

imagen2 = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)

imagen2 = cv2.cvtColor(imagen, cv2.COLOR_BGR2HLS)

plt.imshow(imagen2)
plt.show()