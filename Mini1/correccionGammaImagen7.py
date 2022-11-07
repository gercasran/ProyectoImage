import cv2
import numpy as np
import matplotlib.pyplot as plt

#Apertura de la imagen7
img = cv2.imread('imagen7.jpg')
#Abre pestaña con la imagen7
cv2.imshow('imagen7.jpg',img)
#Esperar una tecla y recibirla en la variable
cv2.waitKey(0)

#Histograma imagen7
hist_full = cv2.calcHist([img],[0],None,[256],[0,256])
plt.plot(hist_full)
plt.title("Histograma imagen7")
plt.show()

#Corrección gamma sobre la imagen7
gamma = 2.5
lookUpTable = np.empty((1,256), np.uint8)
for i in range(256):
    lookUpTable[0,i] = np.clip(pow(i / 255.0, gamma) * 255.0, 0, 255)

res = cv2.LUT(img, lookUpTable)

cv2.imshow('img7_Corregida',res)
#Esperar una tecla y recibirla en la variable
cv2.waitKey(0)

#Histograma imagen corregida
hist_full2 = cv2.calcHist([res],[0],None,[256],[0,256])
plt.plot(hist_full2)
plt.title("Histograma imagen corregida")
plt.show()

cv2.destroyAllWindows()