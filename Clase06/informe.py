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

def leer_precios(nombre_archivo): #Devuelve un diccionario
    f = open(nombre_archivo, 'r')
    rows = csv.reader(f)
    diccionario={}
    for row in rows: #Devuelve una lista ['Fruta', 'precio']
        try:
            diccionario.update({row[0]: float(row[1])})
        except:
            continue
    return diccionario




#print(leer_precios())

#print(leer_camion())
def informe():
    #camion = leer_camion('../Data/camion.csv')
    camion = leer_camion('../Data/fecha_camion.csv')
    precios = leer_precios('../Data/precios.csv')
    costo_venta = 0.0
    costo_camion = 0.0
    #Salida personalizada de filas cabecera
    print(f"Fruta{' '*7}cant{' '*2}p.camion{' '*2}p.venta{' '*3}ganancia")
    for empaque in camion:
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
#print(leer_camion('../Data/missing.csv'))