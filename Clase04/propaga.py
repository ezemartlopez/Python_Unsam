#Esta funcion convierte la lista en una cadena intercambiando el -1 con una coma
def lista_toString(lista):
    string = ''.join([',' if palillo ==-1 else str(palillo) for palillo in lista])
    return string

def reformat_list(cadena):
    lista = [int(letra) for letra in cadena]
    return lista

#al aplicar la anterior funcion obtengo las sublistas 
def separar_filas(lista):
    filas = lista_toString(lista)
    subfilas = filas.split(',')
    return subfilas

def propagar(lista):
    #ejemplo de lista [0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0]
    #otro ejemplo es [ 0, 0, 0, 1, 0, 0]

    #Mi idea es hacer una funcion que separe la lista en sublistas a partir de -1, como separador de filas que pueden o no pueden quemarse
    #Por el momento voy a trabajar con cadenas luego lo reformateo
    subfilas = separar_filas(lista)
    cont_filas = len(subfilas)-1
    resultado = []
    for fila in subfilas:
        if '1' in fila:
            resultado += reformat_list(fila.replace('0','1'))
        else:
            resultado += reformat_list(fila)
        if cont_filas >= 1:
            resultado += [-1]
            cont_filas -= 1

    return resultado


                
if __name__ == "__main__":
    print(">>> propagar([ 0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0])")
    print(propagar([0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0]))
    print(">>> propagar([ 0, 0, 0, 1, 0, 0])")
    print(propagar([ 0, 0, 0, 1, 0, 0]))
    print(">>> propagar([ 1, 0, 0,-1, 0, 0, 0,-1, 0, 1, 0, 0,-1, 0])")
    print(propagar([ 1, 0, 0,-1, 0, 0, 0,-1, 0, 1, 0, 0,-1, 0]))
