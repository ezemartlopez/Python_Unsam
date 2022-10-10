import csv

def format_row(row):
    """Cambia el formato de una lista que se leyo de un archivo csv"""
    aux = []
    aux.append((row[0]))  
    aux.append(int(row[1]))  
    aux.append(float(row[2]))
    return aux

def leer_camion(nombre_archivo):
    """Lee el contenido de un camion en un arhivo csv"""
    lista=[]
    f = open(nombre_archivo)
    rows = csv.reader(f)
    header = next(rows) #obtengo las cabeceras del archivo
    for row in rows:
        diccionario = {}
        new_row = format_row(row) #cambio el formato de las row, es especifico para este caso
        for indice in range(0,3): #accedo a los indices 0 1 2
            diccionario.update({header[indice]:new_row[indice]})
        lista.append(diccionario)

    return lista

def leer_precios(nombre_archivo):
    """Devuelve un diccionario donde las claves son el nombre de fruta y el valor su precio, que lee de un archivo csv"""
    f = open(nombre_archivo, 'r')
    rows = csv.reader(f)
    diccionario={}
    for row in rows: #Devuelve una lista ['Fruta', 'precio']
        try: #captura las lineas vacias en escencia
            diccionario.update({row[0]: float(row[1])})
        except:
            pass #como no se como lidiar con las excepciones solo paso de largo
    return diccionario



def informe():
    """Realiza un informe leyendo dos archivos csv especificos y realiza un informe comparando costo ganancia"""
    camion = leer_camion('../Data/camion.csv')
    precios = leer_precios('../Data/precios.csv')
    costo_venta = 0.0
    costo_camion = 0.0
    # Imprimo las cabeceras del informe
    print(f"Fruta{' '*7}cant{' '*2}p.camion{' '*2}p.venta{' '*3}ganancia")
    for empaque in camion: #el empaque consta de tres cosas nombre_fruta, precio_fruta y cant_cajones
        fruta = empaque['nombre']
        precio = empaque['precio']    
        cajones = empaque['cajones']
        precio_c = round(precio*cajones,2)
        precio_v = round(precios[fruta]*cajones,2)
        #Muestra por salida personalizada todos los valores obtenidos
        print(f"{fruta}{' '*(12-len(fruta))}{cajones}{' '*(6-len(str(cajones)))}{precio_c}{' '*(10-len(str(precio_c)))}{precio_v}{' '*(10-len(str(precio_v)))}{round(precio_v-precio_c,2)}")
        costo_camion += precio_c
        costo_venta += precio_v
            

    print(f"El costo del camion es de: {costo_camion}")
    print(f"Total en ventas de frutas es de: {costo_venta}")
    if (costo_venta-costo_camion) >= 0:
        print(f"La ganancia es de {round(costo_venta-costo_camion,2)}")
    else:
        print(f"La perdida es de {round(costo_venta-costo_camion,2)}")

if __name__=="__main__":
    informe()