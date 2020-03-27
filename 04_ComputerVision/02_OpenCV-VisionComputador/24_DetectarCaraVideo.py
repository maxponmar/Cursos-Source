import numpy as np
import matplotlib.pyplot as plt
import  cv2

cascada_cara = cv2.CascadeClassifier('00_Ficheros/haarcascade_eye.xml')

def detectar_cara(imagen):
    imagen1 = imagen.copy()
    rectangulos = cascada_cara.detectMultiScale(imagen1)
    for (x,y,w,h) in rectangulos:
        cv2.rectangle(imagen1, (x,y), (x+w,y+h),(255,0,0),3)
    return imagen1


captura = cv2.VideoCapture(0)

while True:
    resultado, video = captura.read(0)
    video = detectar_cara(video)
    cv2.imshow('Detectar cara en video', video)
    tecla = cv2.waitKey(1)
    if tecla == 27:
        break

captura.release()
cv2.destroyAllWindows()