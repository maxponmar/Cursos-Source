import matplotlib.pyplot as plt
import numpy as np
import cv2

ajedrez = cv2.imread('00_Ficheros/tableroAjedrez.png')
ajedrez_gris = cv2.cvtColor(ajedrez, cv2.COLOR_BGR2GRAY)


esquinas = cv2.goodFeaturesToTrack(ajedrez_gris, 100, 0.01, 10)
esquinas = np.int0(esquinas)

for i in esquinas:
    x,y = i.ravel()
    cv2.circle(ajedrez, (x,y), 4, (255,0,0),8)

plt.imshow(ajedrez)
plt.show()