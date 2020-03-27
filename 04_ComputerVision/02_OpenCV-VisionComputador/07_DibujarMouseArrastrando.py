import numpy as np
import matplotlib.pyplot as plt
import cv2

# Global variables
dibujando = False
valorx = 0
valory = 0

# Draw function
def dibujar(event, x, y, etiquetas, parametros):
    global dibujando, valorx, valory

    if event == cv2.EVENT_LBUTTONDOWN:
        dibujando = True
        valorx = x
        valory = y
    elif event == cv2.EVENT_MOUSEMOVE:
        if dibujando == True:
            cv2.rectangle(imagen, (valorx,valory), (x,y), (255,0,0), -1)
    elif event == cv2.EVENT_LBUTTONUP:
        dibujando = False
        cv2.rectangle(imagen, (valorx,valory), (x,y), (255,0,0), -1)
    
# Link image with draw function
cv2.namedWindow(winname = 'Mi Imagen')
cv2.setMouseCallback('Mi Imagen', dibujar)


# Show image
imagen = np.zeros(shape = (500,500,3), dtype = np.int8)

while True:
    cv2.imshow('Mi Imagen', imagen)
    # Press scape
    if cv2.waitKey(10) & 0xFF == 27:
        break

cv2.destroyAllWindows()