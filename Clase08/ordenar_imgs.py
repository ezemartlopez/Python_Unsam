import os
import datetime
import time
def obtener_nombre_fecha(fname):
    elementos_nombre = fname.split('_')
    nombre = ''
    if len(elementos_nombre)>2:
        for fragmento_name in elementos_nombre[:-1]:
            nombre += fragmento_name
    else:
        nombre = elementos_nombre[0]
    nombre += '.png'
    fecha = elementos_nombre[-1][:-4]
    return (nombre,fecha)
def style_path(ruta):
    return ruta.replace("\\",'/')
def procesar_nombre(fname):
    elementos_nombre = obtener_nombre_fecha(fname)
    nombre = elementos_nombre[0]
    fecha = elementos_nombre[1]
    anio = int(fecha[:4])
    mes = int(fecha[4:6])
    dia = int(fecha[6:])
    ult_modificacion = datetime.datetime(year = anio, month = mes, day=dia, hour = 0,minute = 0)
    return (nombre,ult_modificacion)

def unir_dir(ruta_base,destino):
    if ruta_base!='':
        return ruta_base + '/' + destino
    else:
        return destino

def borrar_carpetas_vacias(ruta):
    for root, dirs, files in os.walk(ruta):
        for name in dirs:
            root_dir = style_path(os.path.join(root, name))
            try:
                os.rmdir(root_dir)
                #print(f"Se Borro: {root_dir}")
            except WindowsError:
                continue #print(f"No se puede borrar: {root_dir}")


def mover_imagenes(dir_base,dir_destino):
    crear_carpeta(dir_destino)
    for root, dirs, files in os.walk(dir_base):
        for name in files:
            if '.png' in name:
                tname = procesar_nombre(name)
                ruta = style_path(os.path.join(root,name))
                acceso = (datetime.datetime.now()).timestamp()
                modific = tname[1].timestamp()
                os.utime(ruta,(acceso,modific))
                ruta_destino = style_path(os.path.join(dir_destino,tname[0]))
                os.rename(ruta,ruta_destino)
    borrar_carpetas_vacias(dir_base)


def crear_carpeta(destino,printProcess=False):
    """Recibe una ruta y crea un la carpeta necesaria"""
    partes = destino.split('/')
    path_d = ''
    aux = ''
    for parte in partes:
        aux = unir_dir(path_d,parte)
        if not os.path.isdir(aux):
            if printProcess:
                print(f"Path: {path_d}")
                print(f"Se crea la carpeta: {parte}")
            os.chdir(path_d)
            os.mkdir(parte)
        path_d = aux
    return
if __name__=='__main__':
    import sys
    if len(sys.argv)==3:
        ruta_base = sys.argv[1]
        ruta_destino = sys.argv[2]
        mover_imagenes(ruta_base,ruta_destino)
    else:
        print("numero incorrecto de argumentos en linea de comandos")
    #mover_imagenes('../Data/ordenar' '../Data/imgs_procesadas/') 