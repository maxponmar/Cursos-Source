import numpy as np
import matplotlib.pyplot as plt
import  cv2

imagen = cv2.imread('00_Ficheros/perro.jpg')

print("Type: ")
print(type(imagen))
print("Size: ")
print(imagen.shape)

# By default OpenCv use BGR format so the image looks different
plt.imshow(imagen)
plt.show()

# To due with that we convert from BGR 2 RGB
imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
plt.imshow(imagen)
plt.show()

# Gray scale image
imagenGrayScale = cv2.imread('00_Ficheros/perro.jpg', cv2.IMREAD_GRAYSCALE)
plt.imshow(imagenGrayScale, cmap = 'gray')
plt.show()