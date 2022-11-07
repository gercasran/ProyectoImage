import cv2
import numpy as np
from matplotlib import pyplot as plt

def histograma(archivo):
    #Imagen Original
    #Apertura de la imagen7
    img = cv2.imread(archivo,0)
    
    #Abre ventana con la imagen
    #cv2.imshow('imagen-original.bmp', imgOriginal)

    #Calculo y despliegue del histograma
    hist = cv2.calcHist([img], [0], None, [256], [0, 256])
    return hist
    

def plotHistograma(histograma):
    plt.plot(histograma)
    plt.xlabel('Intensidad de iluminacion')
    plt.ylabel('Cantidad de pixeles')
    
def mostrarImagen(archivo, titulo):
    cv2.imshow(titulo, archivo)

def main():
    histo = histograma('Imagen7.jpg')
    plotHistograma(histo,'Imagen7')

if __name__ == "__main__":
    main()




