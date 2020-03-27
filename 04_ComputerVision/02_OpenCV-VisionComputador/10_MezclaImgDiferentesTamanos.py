import matplotlib.pyplot as plt
import cv2

imagen1 = cv2.imread('00_Ficheros/perro.jpg')
imagen1 = cv2.cvtColor(imagen1, cv2.COLOR_BGR2RGB)

imagen2 = cv2.imread('00_Ficheros/logo.jpg')
imagen2 = cv2.cvtColor(imagen2, cv2.COLOR_BGR2RGB)

imagen2 = cv2.resize(imagen2, (1920,300))

# Cut image1 chunk

parteImagen1 = imagen1[:300]

parteImagenMezcla = cv2.addWeighted(src1=parteImagen1, alpha=0.7,src2=imagen2,beta=0.3, gamma=0)

imagen1[:300] = parteImagenMezcla

plt.imshow(imagen1)
plt.show()