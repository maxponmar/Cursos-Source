import matplotlib.pyplot as plt
import cv2

imagen1 = cv2.imread('00_Ficheros/perro.jpg')
imagen1 = cv2.cvtColor(imagen1, cv2.COLOR_BGR2RGB)

imagen2 = cv2.imread('00_Ficheros/marcaAgua.jpg')
imagen2 = cv2.cvtColor(imagen2, cv2.COLOR_BGR2RGB)

imagen1 = cv2.resize(imagen1, (1200,1200))
imagen2 = cv2.resize(imagen2, (1200,1200))

imagenMezcla = cv2.addWeighted(src1=imagen1, alpha=0.5, src2=imagen2, beta = 0.5, gamma = 0)
imagenMezcla = cv2.resize(imagenMezcla, (1920,1280))

plt.imshow(imagenMezcla)
plt.show()