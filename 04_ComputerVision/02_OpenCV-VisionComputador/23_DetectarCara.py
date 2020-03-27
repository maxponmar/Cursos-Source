
import numpy as np
import matplotlib.pyplot as plt
import cv2

rostro1 = cv2.imread('00_Ficheros/epales2.jpg', 0)

familia = cv2.imread('00_Ficheros/familia.png', 0)

cascada_cara = cv2.CascadeClassifier('00_Ficheros/haarcascade_frontalface_default.xml')

def detectar_cara(imagen):
    imagen1 = imagen.copy()
    rectangulos = cascada_cara.detectMultiScale(imagen1)
    for (x,y,w,h) in rectangulos:
        cv2.rectangle(imagen1, (x,y), (x+w,y+h),(255,0,0),3)
    return imagen1

resultado1 = detectar_cara(rostro1)
plt.imshow(resultado1, cmap='gray')
plt.show()

resultado2 = detectar_cara(familia)
plt.imshow(resultado2, cmap='gray')
plt.show()
