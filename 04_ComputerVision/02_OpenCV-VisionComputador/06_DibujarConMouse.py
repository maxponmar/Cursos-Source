import numpy as np
import matplotlib.pyplot as plt
import cv2

# Draw function
def dibujar(event, x, y, etiquetas, parametros):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(imagen, (x,y), 50, (255,0,0), -1)
    
# Link image with draw function
cv2.namedWindow(winname = 'Mi Imagen')
cv2.setMouseCallback('Mi Imagen', dibujar)


# Show image
imagen = np.zeros(shape = (500,500,3), dtype = np.int16)

while True:
    cv2.imshow('Mi Imagen', imagen)
    # Press scape
    if cv2.waitKey(10) & 0xFF == 27:
        break

cv2.destroyAllWindows()