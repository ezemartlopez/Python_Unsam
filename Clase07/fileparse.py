# fileparse.py
import csv
import gzip

def parse_csv(archivo, select = None, types = None, has_headers=True,silence_errors=False):
    '''
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select,
    que debe ser una lista de nombres de las columnas a considerar.
    '''
    filas = None
    is_archivo = isinstance(archivo,str)
    
    if is_archivo:#si el archivo es un string lo trato como nombre de archivo
        is_gzip = '.gz' in archivo
        if is_gzip:
            f = gzip.open(archivo, 'rt')
            filas = csv.reader(f)
        else:
            f = open(archivo)
            filas = csv.reader(f)
        
    else: #sino como en el ejemplo una lista de cadenas con limtador 'coma'
        filas = csv.reader(archivo, delimiter=',')
    registros = []
        # Lee los encabezados del archivo
    try:
        if has_headers:
            encabezados = next(filas)
        else:
            if select != None:
                raise RuntimeError("Para seleccionar, necesito encabezados.")
            # Si se indicó un selector de columnas,
            #    buscar los índices de las columnas especificadas.
            # Y en ese caso achicar el conjunto de encabezados para diccionarios

        if select:
            indices = [encabezados.index(nombre_columna) for nombre_columna in select]
            encabezados = select
        else:
            indices = []

        cont = 0
        for fila in filas:
            try:#Captura excepciones como con el archivo '../Data/missing.csv'
                cont +=1 
                if not fila:    # Saltear filas vacías
                    continue
                # Filtrar la fila si se especificaron columnas
                if indices:
                    fila = [fila[index] for index in indices]
                if types:
                    fila = [func(val) for func, val in zip(types, fila) ]
                # Armar el diccionario
                if has_headers:
                    registro = dict(zip(encabezados, fila))
                else:
                    registro = tuple(fila)
                registros.append(registro)
                                   
            except ValueError as e:
                if silence_errors:
                    continue
                else:
                    print(f"Fila {cont}: No pude convertir la fila {fila} ")
                    print(f"Fila {cont}: Motivo: {e}")
    except Exception as e:
        print("Hubo un error: ",e)
    if is_archivo:
        f.close()
                
    return registros

if __name__=="__main__":
    print(parse_csv('../Data/camion.csv.gz', types=[str,int,float]))
    #print(parse_csv('../Data/precios.csv', select = ['nombre','precio'], has_headers = False))
    #print(parse_csv('../Data/precios.csv', types = [str, float],silence_errors=False))
    lines = ['nombre,cajones,precio', 'Lima,100,34.23', 'Naranja,50,91.1', 'Mburucuya,75,45.1']
    print(parse_csv(lines, types=[str,int,float]))