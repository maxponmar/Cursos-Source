import numpy as np
import matplotlib.pyplot as plt
import cv2

imagen = np.zeros((300,600))
fuente = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(imagen, text='ABCDE', org=(50,200), fontFace=fuente, fontScale=5, color=(255,255,255), thickness=8)

nucleo = np.ones((5,5), dtype=np.uint8)

imagen2 = cv2.erode(imagen, nucleo, iterations=1)

ruido = np.random.randint(low = 0, high = 2, size=(300,600))

ruido = ruido * 255

imagenRuido = imagen+ruido

plt.imshow(imagenRuido, cmap='gray')
plt.show()

imagenSinRuido = cv2.morphologyEx(imagen,cv2.MORPH_OPEN, nucleo)
plt.imshow(imagenSinRuido, cmap='gray')
plt.show()

gradiente = cv2.morphologyEx(imagen, cv2.MORPH_GRADIENT, nucleo)
plt.imshow(gradiente, cmap='gray')
plt.show()