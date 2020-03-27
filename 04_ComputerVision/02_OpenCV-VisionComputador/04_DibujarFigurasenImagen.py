import numpy as np
import matplotlib.pyplot as plt
import cv2

imagen = np.zeros(shape = (500,500,3), dtype = np.int16)
#plt.imshow(imagen)
#plt.show()

cv2.rectangle(imagen, pt1 = (20,20), pt2 = (100,100), color = (0,255,255), thickness = 10)
#plt.imshow(imagen)
#plt.show()

cv2.circle(imagen, center = (250,250), radius = 100, color = (255,0,255), thickness=10)
#plt.imshow(imagen)
#plt.show()

cv2.line(imagen, pt1=(0,400), pt2=(500,400), color=(255,255,0), thickness = 15)
plt.imshow(imagen)
plt.show()