import csv

def format_row(row):
    aux = []
    aux.append((row[0]))  
    aux.append(int(row[1]))  
    aux.append(float(row[2]))
    return aux

def leer_camion(nombre_archivo):
    lista=[]
    f = open(nombre_archivo)
    filas = csv.reader(f)
    encabezados = next(filas)
    for n_fila, fila in enumerate(filas,start=1):
        
        aux_diccionario={}
        diccionario = dict(zip(encabezados,fila))
        #print(diccionario)
        try:
            aux_diccionario.update({'nombre':diccionario['nombre']})
            aux_diccionario.update({'cajones':int(diccionario['cajones'])})
            aux_diccionario.update({'precio':float(diccionario['precio'])})
        except ValueError:
            print(f"Fila {n_fila}: No puede interpretarse: {fila}")
        lista.append(aux_diccionario)
   
    #print(lista)
    return lista

def leer_precios(nombre_archivo):
    """Lee un archivo de precios de frutas y devuelve un diccionario con Clave=fruta y Valor=precio"""
    f = open(nombre_archivo, 'r')
    rows = csv.reader(f)
    diccionario={}
    for row in rows: #Devuelve una lista ['Fruta', 'precio']
        try:
            diccionario.update({row[0]: float(row[1])})
        except:
            continue
    return diccionario


def hacer_informe(camion,precios):
    lista = []
    for empaque in camion:
        nombre = empaque['nombre']
        cajones = empaque['cajones']
        precio_venta = empaque['precio']
        diferencia = precios[nombre] - precio_venta
        tuple_empaque = (nombre,cajones,precio_venta,diferencia)
        lista.append(tuple_empaque)
    
    #print(lista)
    return lista


def informe():
    #camion = leer_camion('../Data/camion.csv')
    camion = leer_camion('../Data/fecha_camion.csv')
    precios = leer_precios('../Data/precios.csv')
    informe = hacer_informe(camion,precios)
    encabezados = ('Nombre','Cajones','Precio','Cambio')
    print('%10s %10s %10s %10s' % encabezados)
    print(f"{'-'*10} {'-'*10} {'-'*10} {'-'*10}")
    for nombre,cajones,precio,cambio in informe:
        print(f"{nombre:>10s} {cajones:>10d} {('$'+str(round(precio,2))):>10s} {cambio:>10.2f}")
if __name__=="__main__":
    informe()
    #print(leer_camion('../Data/fecha_camion.csv'))