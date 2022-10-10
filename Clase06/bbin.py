def busqueda_lineal_lordenada(lista,e):
    """Busqueda Lineal secuencial"""
    pos = -1
    for indice,valor in enumerate(lista):
        if valor == e:
            pos = indice
        elif e >valor:
            continue
        else:
            break
    return pos
def busqueda_binaria(lista, x, verbose = False):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve -1 si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista
    '''
    if verbose:
        print(f'[DEBUG] izq |der |medio')
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
    return pos

def donde_insertar(lista, x):
    '''Donde_insertar
    recibe una lista ordenada y un elemento y devuelva la posición de ese elemento en la lista
    (si se encuentra en la lista) o la posición donde se podría insertar el elemento para que la 
    lista permanezca ordenada (si no está en la lista).
    '''
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
        
    if pos == -1:    
        pos = medio
    if lista[pos] < x:
        pos += 1   
    return pos

def insertar_posicion(lista,elemento):
    aux = []
    while len(lista) > 0 and elemento < lista[-1]:#basicamente sigue sacando elementos mientras sea menor 
        aux.append(lista.pop(-1))#y los almacena aqui, pero es una pila 
    aux.sort()
    lista.append(elemento)
    lista.extend(aux)

#Me parece que tiene que modificar la lista y devolver la posicion
def insertar(lista, x):
    pos = donde_insertar(lista,x)#Nota me devuelve la posicion indice de lista, puede devolver un indice fuera de rango es decir lo sig.
    if pos == len(lista):# si debo insertar al ultimo de la lista
        lista.append(x)#loagrego al final
    else:
        insertar_posicion(lista,x)
    return pos
    
if __name__=="__main__":
    """
    var = donde_insertar([1,2,3,4,5,6],7)
    print(f"pos: {var}")
    var = donde_insertar([0,1,2,3,4,6],5)
    print(f"pos: {var}")
    """
    #print(donde_insertar([1,2,3,4,5],0))
    """"""
    lista = [1,2,3,5,6]
    print(f"Inicia la lista en: {lista}")
    pos = insertar(lista,4)
    print(f"insertar({lista},4) en pos: {pos}")
    
    print(f"Inicia la lista en: {lista}")
    pos = insertar(lista,7)
    print(f"insertar({lista},7) en pos: {pos}")
    print(f"Inicia la lista en: {lista}")
    pos = insertar(lista,0)
    print(f"insertar({lista},0) en pos: {pos}")
    
    