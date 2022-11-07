#Imagen Original
import cv2
import numpy as np
from matplotlib import pyplot as plt

#Apertura de la imagen7
imgOriginal = cv2.imread('imagen-original.bmp')
#Abre pestaña con la imagen7
cv2.imshow('imagen-original.bmp', imgOriginal)

#Calculo y despliegue del histograma
hist = cv2.calcHist([imgOriginal], [0], None, [256], [0, 256])
plt.plot(hist)
plt.xlabel('Intensidad de iluminacion')
plt.ylabel('Cantidad de pixeles')
plt.show()

cv2.destroyAllWindows()