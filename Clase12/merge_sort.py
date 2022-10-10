import random

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

if __name__=='__main__':
    lista = [6, 0, 3, 2, 5, 7, 4, 1]*4
    new_lista = merge_sort(lista)
    print(new_lista)