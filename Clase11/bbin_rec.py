def bbinaria_rec(lista, e):
    """es una funcion recursiva que implementa la busqueda binaria de un
    elemento 'e' en una lista ordenada 'lista'.  """
    if len(lista) == 0:
        res = False
    elif len(lista) == 1:
        res = lista[0] == e
    else:
        medio = len(lista)//2

        elem_medio = lista[medio]
        #comienza la recursion 
        if e >= elem_medio:
            res=bbinaria_rec(lista[medio:],e)
        else:
            res=bbinaria_rec(lista[:medio],e)

    return res

if __name__=='__main__':
    print(bbinaria_rec([4,6,10,12,17,25,29,30,41,44],44))