import random
import numpy
import matplotlib.pyplot as plt
#=====================SELECCION===========================================
def buscar_max(lista, a, b):
    """Devuelve la posición del máximo elemento en un segmento de
       lista de elementos comparables.
       La lista no debe ser vacía.
       a y b son las posiciones inicial y final del segmento"""

    pos_max = a
    for i in range(a + 1, b + 1):
        if lista[i] > lista[pos_max]:
            pos_max = i
    return pos_max

def ord_seleccion(lista):
    """Ordena una lista de elementos según el método de selección.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""

    # posición final del segmento a tratar
    n = len(lista) - 1
    contador = 0
    # mientras haya al menos 2 elementos para ordenar
    while n > 0:
        # posición del mayor valor del segmento
        p = buscar_max(lista, 0, n)
        contador += n

        # intercambiar el valor que está en p con el valor que
        # está en la última posición del segmento
        lista[p], lista[n] = lista[n], lista[p]
        #print("DEBUG: ", p, n, lista)

        # reducir el segmento en 1
        n = n - 1

    return contador

#=====================INSERCION============================================
def ord_insercion(lista):
    """Ordena una lista de elementos según el método de inserción.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""
    cont = 0
    for i in range(len(lista) - 1):
        # Si el elemento de la posición i+1 está desordenado respecto
        # al de la posición i, reubicarlo dentro del segmento [0:i]
        cont += 1
        if lista[i + 1] < lista[i]:
            
            cont += reubicar(lista, i + 1)
        #print("DEBUG: ", lista)

    return cont

def reubicar(lista, p):
    """Reubica al elemento que está en la posición p de la lista
       dentro del segmento [0:p-1].
       Pre: p tiene que ser una posicion válida de lista."""

    v = lista[p]

    # Recorrer el segmento [0:p-1] de derecha a izquierda hasta
    # encontrar la posición j tal que lista[j-1] <= v < lista[j].
    j = p
    cont = 0
    while j > 0 and v < lista[j - 1]:
        # Desplazar los elementos hacia la derecha, dejando lugar
        # para insertar el elemento v donde corresponda.
        lista[j] = lista[j - 1]
        j -= 1
        cont += 1

    lista[j] = v
    return cont

#=====================BURBUJEO=============================================
def ord_burbujeo(lista,debug=False):
    """Funciona revisando cada elemento de la lista que va a ser ordenada con el siguiente, 
    intercambiándolos de posición si están en el orden equivocado. Revisa varias veces toda 
    la lista hasta que no se necesiten más intercambios, lo cual significa que la lista está ordenada"""
    no_ordenado = True
    iteraciones = 0 # contador de iteraciones sobre la lista
    limite = 1
    while no_ordenado:
        #comienzo declarando que la lista ya se encuentra ordenada
        no_ordenado = False
        

        for i in range(len(lista)-limite):
            iteraciones += 1
            if lista[i] > lista[i+1]:
                
                #si se encuentra un valor no ordenado realiza un intercambio de lugares
                aux = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = aux
                #cambia la bandera para que itere sobre la lista otra vez
                no_ordenado = True
        limite += 1
    if debug:
        print(f"cantidad de comparaciones {iteraciones}")
    return iteraciones

#=====================MERGE SORT=============================================
def merge_sort(lista):
    """Ordena lista mediante el método merge sort.
       Pre: lista debe contener elementos comparables.
       Devuelve: una nueva lista ordenada."""
    
    cont = 0
    def recursion_merge(lista):
        nonlocal cont
        #
        if len(lista) < 2:
            lista_nueva = lista
        else:
            medio = len(lista) // 2
            izq = recursion_merge(lista[:medio])
            der = recursion_merge(lista[medio:])
            lista_nueva,var= merge(izq, der)
            cont += var
        return lista_nueva
    recursion_merge(lista)
    #print(nueva)
    return cont

def merge(lista1, lista2):
    """Intercala los elementos de lista1 y lista2 de forma ordenada.
       Pre: lista1 y lista2 deben estar ordenadas.
       Devuelve: una lista con los elementos de lista1 y lista2."""
    i, j = 0, 0
    resultado = []
    cont = 0
    while(i < len(lista1) and j < len(lista2)):
        cont += 1
        if (lista1[i] < lista2[j]):
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1

    # Agregar lo que falta de una lista
    resultado += lista1[i:]
    resultado += lista2[j:]

    return resultado,cont
#==================================================================
def generar_lista(N):
    minimo = 1
    maximo = 1000
    lista = [random.randint(minimo,maximo) for i in range(N)]
    return lista

def promedio_lista(lista):
    return sum(lista)/len(lista)

def experimento(N, k):
    """La funcion retorna una tupla con el promedio de una lista de largo N y que se repite 
    k veces. (burbujeo, inserción, selección y merge_sort)"""
    lista_seleccion = []
    lista_insercion = []
    lista_burbujeo = []
    lista_merge_sort = []
    for i in range(k):
        lista_exp = generar_lista(N)
        lista_burbujeo.append(ord_burbujeo(lista_exp.copy()))
        lista_insercion.append(ord_insercion(lista_exp.copy()))
        lista_seleccion.append(ord_seleccion(lista_exp.copy()))
        lista_merge_sort.append(merge_sort(lista_exp.copy()))
    return (promedio_lista(lista_burbujeo),promedio_lista(lista_insercion),promedio_lista(lista_seleccion),promedio_lista(lista_merge_sort))

def experimento_vectores(Nmax):
    """Devuelve una lista de tuplas con los experimentos de listas de longitud N, entre 1 y Nmax """
    lista_comparaciones = [experimento(N,1) for N in range(Nmax)]
    return lista_comparaciones
    
def principal(largo_lista):
    largo  = largo_lista
    lista = experimento_vectores(largo)
    lista_burbujeo = []
    lista_insercion = []
    lista_seleccion = []
    lista_merge = []
    for tupla in lista:
        lista_burbujeo.append(tupla[0])
        lista_insercion.append(tupla[1])
        lista_seleccion.append(tupla[2])
        lista_merge.append(tupla[3])
    eje_x = [i for i in range(largo)]
    #plt.plot(lista1, marker='x', linestyle=':', color='b', label = "Enero")
    plt.plot(eje_x,lista_burbujeo,color='g',label='Burbujeo')

    plt.plot(eje_x,lista_insercion,color='b',linestyle='--',label='insercion')

    plt.plot(eje_x,lista_seleccion,color='r',linestyle=':',label='seleccion')

    plt.plot(eje_x,lista_merge,label='merge_sort')
    plt.legend(loc='upper left')
    plt.show()

if __name__=='__main__':
    principal(500)