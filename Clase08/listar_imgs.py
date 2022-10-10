import os
import sys

def archivos_png(directorio):
    """Arma una lista de todos los archivos .png que se encuentren en algún subdirectorio directorio dado"""
    os.chdir(directorio)#cambio al directorio especificado
    lista_imagenes = []
    for root, dirs, files in os.walk("."):
        for name_file in files:
            if '.png' in name_file:
                lista_imagenes.append(name_file)
    return lista_imagenes

if __name__=='__main__':
    if len(sys.argv) == 2:
        print(archivos_png(sys.argv[1]))
    else:
        print('Falta el nombre del archivo')
        