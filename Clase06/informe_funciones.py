from fileparse import parse_csv

def leer_camion(nombre_archivo):
    """
    Devuelve una lista de diccionarios con las claves nombre, cajones y precio
    """
    camion = parse_csv(nombre_archivo, select = ['nombre', 'cajones', 'precio'], types = [str, int, float])
    return camion

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

def informe_camion():
    archivo_c = '../Data/fecha_camion.csv'
    archivo_p = '../Data/precios.csv'
    camion = leer_camion(archivo_c)
    precios = leer_precios(archivo_p)
    cabeceras = ['nombre','cajones','precio']
    imprimir_fila(cabeceras+['cambio'],15)#imprimo las cabeceras en una fila mas la columna de diferencia
    imprimir_fila([f"{'-'*14}" for i in range(4)],15)#Imprimo separadores -------- 
    for empaque in camion:#Basicamente leo cada empaque del camion y lo coloco en una lista para ser impresa por Imprimir_fila()
        fila = [empaque[indice] for indice in cabeceras]#aqui se agrega ala lista solo los valores de las claves en las cabeceras
        diferencia = round(precios[fila[0]] - fila[2],2)#hago la diferencia entre precios de camion y de venta
        fila[2]=f"${fila[2]}"#cambio el formato de precio a: $precio
        fila += [diferencia] #agrego la diferencia a la lista 
        imprimir_fila(fila,15)#imprimo cada elem de la lista ocupando cada uno 15 espacios

if __name__=="__main__":
    informe_camion()