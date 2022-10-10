import csv
import sys
def costo_camion(nombre_archivo):
    """Lee un archivo csv que puede contener datos faltantes y devuelve el costo total del camion"""
    f = open(nombre_archivo)
    rows = csv.reader(f)
    header = next(rows) #Obtengo los headers del archivo
    total = 0 #guardo la suma de los costos de las frutas
    for row in rows:
        try: #capturo excepciones al leer una linea incompleta, es decir le falta el stock
            cajas=int(row[1])
            precio=float(row[2])
            total = total + cajas*precio
        except ValueError:
            print(f"{row[0]} no cuenta con stock.")
            
    return total
if __name__=="__main__":

    #comprobando la linea de comandos
    if len(sys.argv)==2:
        nombre_archivo = sys.argv[1]
    else:
        nombre_archivo = '../Data/camion.csv'

    costo = costo_camion(nombre_archivo)
    print(f"Costo total: {costo}")
