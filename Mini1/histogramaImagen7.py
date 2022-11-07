#Imagen 7
import cv2
import numpy as np
from matplotlib import pyplot as plt

#Apertura de la imagen
img = cv2.imread('imagen7.jpg')
#Abre pestaña con la imagen
cv2.imshow('imagen7.jpg', img)

#Calculo y despliegue del histograma
hist = cv2.calcHist([img], [0], None, [256], [0, 256])
plt.plot(hist)
plt.xlabel('Intensidad de iluminacion')
plt.ylabel('Cantidad de pixeles')
plt.show()

cv2.destroyAllWindows()