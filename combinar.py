"""
Programa para combinar dos imágenes usando una máscara

Elaborado por Joaquín Martíez

"""

#Este comentario es para probar git
import cv2 as cv
import numpy as np


def applyMask(img, mask):
    rows = img.shape[0]
    cols = img.shape[1]

    newImage = img.copy() #Crea una copia de la imagen de entrada

    for i in range(0, rows):   #Recorre las filas de la imágen
        for j in range(0, cols):    #Recorre las columnas de cada fila
            if(mask[i,j] == 0):       #Si el valor de la máscara en el pixel i,j es 0, pone los canales de la imagen en 0
                newImage.itemset((i,j,0), 0)
                newImage.itemset((i,j,1), 0)
                newImage.itemset((i,j,2), 0)

    return newImage #Regresa la imagen con la máscara aplicada


I_background = cv.imread('fondo.bmp')  #Lee la imagen a usar de fondo en BGR
I_body = cv.imread('greenscreen.bmp')  #Lee la imagen a usar en cuerpo en BGR
I_mask = cv.imread('greenscreenMask.bmp', cv.IMREAD_GRAYSCALE)   #Lee la máscara (en escala de grises)

ret, I_mask_bin = cv.threshold(I_mask, 100, 255, cv.THRESH_BINARY) #Binariza la máscara a usar (por si hay pixeles no en 0 o 255)
newBody = applyMask(I_body, I_mask_bin)  #Le aplica la máscara a la imagen

mask_inverted = 255 - I_mask_bin   #Invierte la máscara original para sacar el complementos
newBackground = applyMask(I_background, mask_inverted)  #Le aplica la máscara invertida al fondo

newImage = newBody + newBackground  #Suma las imagenes en una sola

cv.imshow('Nueva imagen', newImage)  #Muestra la imagen terminadas

cv.waitKey(0)

cv.destroyAllWindows()
