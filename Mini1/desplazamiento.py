#Imagen Original
import cv2
import numpy as np
from matplotlib import pyplot as plt
from histograma import *


def desplazar(imagen,cantidad):
    #Apertura de la imagen7
    img = cv2.imread(imagen,0)
    #Desplazamiento a sumar en cada pixel
    desplazamiento = cantidad
    #Creación de una tabla nueva que contenga los valores modificados
    nuevaTabla = np.empty((1,256), np.uint8)
    for i in range(256):
        nuevaTabla[0,i] = np.clip(i + desplazamiento, 0, 255)
    #Reconstruir la imagen nueva mediante la nueva tabla 
    desplazada = cv2.LUT(img, nuevaTabla)
    #Histograma imagen corregida
    histogramaDesplazado = cv2.calcHist([desplazada],[0],None,[256],[0,256])
    #Retorna una tupla con la imagen desplazada y su histograma
    return desplazada, histogramaDesplazado


def main():
    nombreImagen = 'Imagen7.jpg'
    imagenOriginal = cv2.imread(nombreImagen)
    imagenDes,histogramaDes = desplazar(nombreImagen, -30)
    mostrarImagen(imagenDes, 'Imagen desplazada')
    mostrarImagen(imagenOriginal, 'Imagen original')
    histogramaImagen = histograma(nombreImagen)
    plotHistograma(histogramaImagen)
    plotHistograma(histogramaDes)
    plt.title('Histogramas')
    plt.legend(['Original','Desplazada'])
    plt.show()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

