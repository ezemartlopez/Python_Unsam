#Desde mi punto de vista no es necesario aplicar try y catch ya que el archivo no presenta un elemento vacio
def buscar_precio(fruta):
    """Busca el precio de una fruta en un archivo csv especifico, y lo imprime por pantalla si lo encuentra o no"""
    f=open('../Data/precios.csv','rt')
    precio=0
    no_existe_fruta=True
    for line in f:
        row=line.split(',') #Cada linea del archivo tiene formato FRUTA,PRECIO.
        nombre=row[0] #accedo al nombre de fruta
        if nombre==fruta:
            precio=row[1] #accedo al precio de la fruta
            no_existe_fruta=False #cambio la bandera indicando que existe
            print(f"El precio de {fruta} es: {precio}")
    if no_existe_fruta:
        print(f"{fruta} no figura en el listado")
    f.close()
    
if __name__=="__main__":
    buscar_precio('Frambuesa')
    buscar_precio('Kale')