def tribonacci(signature, n):
    #your code here
    lista = []
    aux = signature.copy()
    cont = 0
    num = 0
    while cont < n:
        if len(lista) < 3:
            lista.append(aux[cont])
        else:
            lista.append(sum(lista[m:])
            num += 1
        cont = cont + 1
    return lista