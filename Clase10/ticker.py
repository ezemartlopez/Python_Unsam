# ticker.py

from vigilante import vigilar
import formato_tabla
import csv
import informe_final
def elegir_columnas(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]

def cambiar_tipo(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]

def hace_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))

def parsear_datos(lines):
    """Recibe un iterable de un generador como vifilar(), y devuelve
    un iterable creado por una expresion generadora que devuelve los tres
    primeros elementos de cada linea del iterable"""
    rows = csv.reader(lines)
    #elijo las columnas([0, 1, 2])
    rows = ([r[indice] for indice in [0, 1, 2]] for r in rows)
    #rows es un iterable de listas , ej iterable(['nombre','precio','volumen'], ...)
    return rows

def filtrar_datos(rows, nombres):
    for row in rows:
        if row['nombre'] in nombres:
            yield row
            
def imprimir_el_informe(data,formateador,encabezados):
    """data es un iterable de listas 
    iterable(['nombre', 'precio', 'volumen'], ...)"""
    #establezco los encabezados del formateador
    formateador.encabezado(encabezados)

    for lista in data:
        #a traves del metodo fila del formateador le paso cada fila que leo de data y lo imprime siguiendo
        # el formato que tiene la clase formateador.
        formateador.fila(lista)

def ticker(camion_file, log_file, fmt):
    camion = informe_final.leer_camion(camion_file)
    #aun recurro a parsear datos, pero utiliza una expresion generadora
    rows = parsear_datos(vigilar(log_file))
    #filtra los datos del iterable, almacena solo los que se encuentran en camion
    rows = (row for row in rows if row[0] in camion)
    # Elige el formato
    if fmt == 'txt':
        formateador = formato_tabla.FormatoTablaTXT()
    elif fmt == 'csv':
        formateador = formato_tabla.FormatoTablaCSV()
    elif fmt == 'html':
        formateador = formato_tabla.FormatoTablaHTML()
    else:
        raise RuntimeError(f'Unknown format {fmt}')
    #por ultimo derivo a una funcion que imprime segun un formato y encabezados
    imprimir_el_informe(rows,formateador,['Nombre', 'Precio', 'Volumen'])

if __name__ == '__main__':
    ticker('../Data/camion.csv','../Data/mercadolog.csv','txt')
    