import numpy as np
import matplotlib.pyplot as plt
import cv2

imagen = cv2.imread('00_Ficheros/sudoku.jpg', 0)

sobelx = cv2.Sobel(imagen, cv2.CV_64F, 1, 0, ksize = 5)
sobely = cv2.Sobel(imagen, cv2.CV_64F, 0, 1, ksize = 5)

imagen2 = cv2.addWeighted(src1 = sobelx, alpha = 0.5, src2 = sobely, beta = 0.5, gamma = 0)
plt.imshow(imagen2, cmap='gray')
plt.show()

laplacian = cv2.Laplacian(imagen, cv2.CV_64F)
plt.imshow(laplacian, cmap='gray')
plt.show()