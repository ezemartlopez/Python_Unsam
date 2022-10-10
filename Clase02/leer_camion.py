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
    header = next(rows) #Obtengo las cabeceras del archivo
    for row in rows:
        diccionario = {}
        new_row = format_row(row) #Formateo las lineas
        for indice in range(0,3): #accedo a los indices 0 1 2
            diccionario.update({header[indice]:new_row[indice]})
        lista.append(diccionario)
   
    #print(lista)
    return lista

if __name__=="__main__":
    print(leer_camion('../Data/camion.csv'))