#Imagen Original
import cv2
import numpy as np
from matplotlib import pyplot as plt
from histograma import *


def contraer(imagen,minimoDeseado,maximoDeseado):
    #Apertura de la imagen7
    img = cv2.imread(imagen,0)
    #Creación de una tabla nueva que contenga los valores modificados
    nuevaTabla = np.empty((1,256), np.uint8)
    #Calculo de minimo y maximo locales
    minLocal = np.amin(img)
    maxLocal = np.amax(img)

    for i in range(256):
        nuevaTabla[0,i] = np.clip((maximoDeseado-minimoDeseado)/(maxLocal-minLocal)*(i-minLocal)+minimoDeseado, 0, 255)
    #Reconstruir la imagen nueva mediante la nueva tabla 
    contraida = cv2.LUT(img, nuevaTabla)
    #Histograma imagen corregida
    histogramaContraido = cv2.calcHist([contraida],[0],None,[256],[0,256])
    #Retorna una tupla con la imagen desplazada y su histograma
    return contraida, histogramaContraido


def main():
    nombreImagen = 'Imagen7.jpg'
    imagenOriginal = cv2.imread(nombreImagen)
    imagenCon,histogramaCon = contraer(nombreImagen,20,120)
    mostrarImagen(imagenCon, 'Imagen contraida')
    mostrarImagen(imagenOriginal, 'Imagen original')
    histogramaImagen = histograma(nombreImagen)
    plotHistograma(histogramaImagen)
    plotHistograma(histogramaCon)
    plt.title('Histogramas')
    plt.legend(['Original','Contraida'])
    plt.show()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

