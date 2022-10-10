import csv
import formato_tabla
from fileparse import parse_csv
from lote import Lote
import sys
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

def hacer_informe(lista_camion,lista_precios):
    #encabezados = ['nombre', 'cantidad', 'precio']
    listado = []
    for lote in lista_camion:
        lista = lote.listar_variables()
        diferencia = lista[1]*lista[2] #multiplico cajones por precio
        lista.append(diferencia)
        listado.append(tuple(lista))
    return listado

def imprimir_informe(data_informe, formateador):
    '''
    Imprime una tabla prolija desde una lista de tuplas
    con (nombre, cajones, precio, diferencia) 
    '''
    formateador.encabezado(['Nombre', 'Cantidad', 'Precio', 'Cambio'])
    for nombre, cajones, precio, cambio in data_informe:
        rowdata = [nombre, str(cajones), f'{precio:0.2f}', f'{cambio:0.2f}']
        formateador.fila(rowdata)

def informe_camion(archivo_camion, archivo_precios, fmt = 'txt'):
    '''
    Crea un informe con la carga de un camión
    a partir de archivos camion y precio.
    El formato predeterminado de la salida es txt
    Alternativas: csv o html
    '''
    # Leer archivos con datos
    camion = leer_camion(archivo_camion)
    precios = leer_precios(archivo_precios)

    # Obtener los datos para un informe
    data_informe = hacer_informe(camion, precios)

    # Elige formato
    if fmt == 'txt':
        formateador = formato_tabla.FormatoTablaTXT()
    elif fmt == 'csv':
        formateador = formato_tabla.FormatoTablaCSV()
    elif fmt == 'html':
        formateador = formato_tabla.FormatoTablaHTML()
    else:
        raise RuntimeError(f'Unknown format {fmt}')
    imprimir_informe(data_informe, formateador)
def principal(a_camion,a_precios,formato):
    informe_camion(a_camion,a_precios,fmt = formato)

if __name__=='__main__':
    import sys
    if len(sys.argv) == 4:
        arch_camion = sys.argv[1]
        arch_precios = sys.argv[2]
        formato = sys.argv[3]
        principal(arch_camion,arch_precios,formato)
    else:
        print("Numero incorrecto de argumentos en linea de comandos")
    #informe_camion('../Data/camion.csv', '../Data/precios.csv',fmt='html')