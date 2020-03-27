import matplotlib.pyplot as plt
import cv2

imagen = cv2.imread('00_Ficheros/perro.jpg')
imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)

imagen2 = cv2.imread('00_Ficheros/cara.jpg')
imagen2 = cv2.cvtColor(imagen2, cv2.COLOR_BGR2RGB)

metodo = cv2.TM_CCOEFF
resultado = cv2.matchTemplate(imagen, imagen2, metodo)
plt.imshow(resultado)
plt.show()

valor_min, valor_max, pos_min, pos_max = cv2.minMaxLoc(resultado)

alto, ancho, colores = imagen2.shape

top_izq = pos_max
bot_der = (pos_max[0]+ancho,pos_max[1]+alto)

cv2.rectangle(imagen, top_izq, bot_der, (255,0,0), 8)
plt.imshow(imagen)
plt.show()