import numpy as np
import matplotlib.pyplot as plt
import  cv2

imagen = cv2.imread('00_Ficheros/perro.jpg')
imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
plt.imshow(imagen)
#plt.show()
print(imagen.shape)

# Resize
imagen2 = cv2.resize(imagen, (800,600))
plt.imshow(imagen2)
plt.show()

# Porcentage
ratio_ancho = 0.5
ratio_alto = 0.5
imagen2 = cv2.resize(imagen2, (0,0), imagen2, ratio_ancho, ratio_alto)
plt.imshow(imagen2)
plt.show()
print(imagen2.shape)

# Flip
# Horizontal = 1
imagen3 = cv2.flip(imagen2, 1)
plt.imshow(imagen3)
plt.show()
# Vertical = 0
imagen3 = cv2.flip(imagen2, 0)
plt.imshow(imagen3)
plt.show()

# Save file (We need to convert it to BGR again to keep the original color)
imagen3 = cv2.cvtColor(imagen3, cv2.COLOR_RGB2BGR)
cv2.imwrite('00_Ficheros/perro_alreves.jpg', imagen3)