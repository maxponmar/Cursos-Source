# No funciona

import numpy as np
import matplotlib.pyplot as plt
import cv2

cereal = cv2.imread('00_Ficheros/cereal.png')
cereales = cv2.imread('00_Ficheros/cereales.png')

cereal = cv2.cvtColor(cereal, cv2.COLOR_BGR2RGB)
cereales = cv2.cvtColor(cereales, cv2.COLOR_BGR2RGB)

sift = cv2.xfeatures2d.SIFT_create()

kp1,des1 = sift.detectAndCompute(cereal, None)
kp2,des2 = sift.detectAndCompute(cereales, None)

indice = dict(algorithm=0,trees=5)
busqueda = dict(checks=50)

flan = cv2.FlannBasedMatcher(indice,busqueda)
emparejamientos = flan.knnMatch(des1, des2, k=2)

mejores = []
for e1, e2 in emparejamientos:
    if e1.distance < 0.7*e2.distance:
        mejores.append([e1])

imagenEmparejamientos = cv2.drawMatchesKnn(cereal,kp1,cereales,kp2,mejores[0:30],None,flags=0)
imagenEmparejamientos = cv2.cvtColor(imagenEmparejamientos, cv2.COLOR_BGR2RGB)


plt.imshow(imagenEmparejamientos)
plt.show()