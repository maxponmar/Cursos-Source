import numpy as np
import matplotlib.pyplot as plt
import  cv2

imagen1 = cv2.imread('00_Ficheros/perro.jpg')
imagen2 = cv2.cvtColor(imagen1, cv2.COLOR_BGR2RGB)

histo = cv2.calcHist([imagen2],[0],None,[256],[0,256])
plt.plot(histo)
plt.show()

colores = ('b','g','r')

for i,color in enumerate(colores):
    histo = cv2.calcHist([imagen2],[i],None,[256],[0,256])
    plt.plot(histo)
    plt.xlim([0,256])
plt.show()