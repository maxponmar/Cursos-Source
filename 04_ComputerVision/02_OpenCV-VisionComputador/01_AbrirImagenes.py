import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

imagen = Image.open('00_Ficheros/perro.jpg')

print(type(imagen))
print(imagen.size)

arrayImg = np.asarray(imagen)
plt.imshow(arrayImg)
plt.show()

#arrayImg[:,:,0]
#arrayImg[:,:,1]
#arrayImg[:,:,2]
