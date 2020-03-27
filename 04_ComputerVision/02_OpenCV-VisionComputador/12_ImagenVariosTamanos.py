import matplotlib.pyplot as plt
import cv2

imagen = cv2.imread('00_Ficheros/perro.jpg')
imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)

figura = plt.figure(figsize = (10,7))
lienzo = figura.add_subplot(111)
lienzo.imshow(imagen)
plt.show()