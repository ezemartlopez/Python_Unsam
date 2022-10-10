
# me quedo con la version del 2.10 ya que se puede realizar pruebas de manera mas facil
import csv
def costo_camion(nombre_archivo):
    f = open(nombre_archivo)
    rows = csv.reader(f)
    header = next(rows)
    total = 0
    for row in rows:
        try:
            cajas=int(row[1])
            precio=float(row[2])
            total = total + cajas*precio
        except ValueError:
            print(f"{row[0]} no cuenta con stock.")
    return total


costo = costo_camion('../Data/missing.csv')
print(f"Costo total: {costo}")