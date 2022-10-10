from fileparse import parse_csv
from lote import Lote
import sys
#BASICAMENTE NO TUVE QUE HACER NINGUNA MODIFICACION YA parse_csv SE ENCARGA DE LEER LOS ARCHIVOS
#PROCESAR LISTAS, ES DECIR SE ENCARGA DE DETECTAR SI ES UNA LISTA, UN ARCHIVO COMUN O UN ARCHIVO.GZIP
#Y OPERA SIGUIENDO LAS FUNCIONES NORMALES
def leer_camion(nombre_archivo):
    """
    Devuelve una lista de diccionarios con las claves nombre, cajones y precio
    """
    camion = parse_csv(nombre_archivo, select = ['nombre', 'cajones', 'precio'], types = [str, int, float])
    lotes_camion = [Lote(d['nombre'],d['cajones'],d['precio']) for d in camion]
    return lotes_camion

def leer_precios(nombre_archivo):
    """
    Devuelve un diccionario con clave = fruta y un valor = precio
    """
    lista_precios = parse_csv(nombre_archivo, types = [str, float], has_headers = False)
    diccionario = dict(lista_precios)
    return diccionario
def imprimir_fila(lista,separacion):
    #imprime en una fila todos los elementos de la lista con una separacion
    s = ''
    for v in lista:
        largo = len(str(v))
        s += f"{str(v)}{' '*(separacion-largo)}"
    print(s)

def informe_camion(archivo_camion,archivo_precios):
    camion = leer_camion(archivo_camion)
    precios = leer_precios(archivo_precios)
    cabeceras = ['nombre','cajones','precio']

    imprimir_fila(cabeceras+['cambio'],15)#imprimo las cabeceras en una fila mas la columna de diferencia
    imprimir_fila([f"{'-'*14}" for i in range(4)],15)#Imprimo separadores -------- 

    for un_lote in camion:#Basicamente leo cada empaque del camion y lo coloco en una lista para ser impresa por Imprimir_fila()
        fila = un_lote.listar_variables() #aqui se agrega ala lista solo los valores de las claves en las cabeceras
        diferencia = round(precios[fila[0]] - fila[2],2)#hago la diferencia entre precios de camion y de venta
        fila[2]=f"${fila[2]}"#cambio el formato de precio a: $precio
        fila += [diferencia] #agrego la diferencia a la lista 
        imprimir_fila(fila,15)#imprimo cada elem de la lista ocupando cada uno 15 espacios    
    return

def f_principal(argumentos):
    try:
        if len(argumentos) != 3:
            raise SystemExit(f'Uso adecuado: {argumentos[0]} ' 'archivo_camion archivo_precios')
        archivo_c = argumentos[1]
        archivo_p = argumentos[2]
        informe_camion(archivo_c,archivo_p)
    except Exception as e:
        print(e)


if __name__=="__main__":
    import sys
    f_principal(sys.argv)
    
