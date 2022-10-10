def triangular(n):
    if n==1:
        return 1
    return n + triangular(n-1)

def cant_digitos(n):
    if n < 10:
        return 1
    return 1 + cant_digitos(n//10)

def es_potencia(n,b):
    return ""

def pascal(fila,columna):
    """retorna el numero en la fila y columna indicada del triangulo de pascal
    comenzando desde la fila 0 y columna 0"""
    def es_pascal(lista,indice,limite):
        pascal_lista = []
        if indice == 0:
            pascal_lista = [1]
        elif indice == 1:
            pascal_lista = [1,1]
        else:
            aux = [0]+lista+[0]
        
            for i in range(len(aux)-1):
                pascal_lista.append(aux[i]+aux[i+1])

        if indice == limite:
            return [pascal_lista]
        return [pascal_lista] + es_pascal(pascal_lista,len(pascal_lista),limite)
    pascal = es_pascal([],0,fila)
    return pascal[fila][columna]

        

if __name__=='__main__':
    #n = 4
    #print(f"el triangular de {n} es {triangular(n)}")
    #n = 123
    #print(f"la cantidad de digitos de {n} es {cant_digitos(n)}")
    print(pascal(5,1))
