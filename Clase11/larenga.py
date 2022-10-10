def pascal(fila,columna):
    """retorna el numero en la fila y columna indicada del triangulo de pascal
    comenzando desde la fila 0 y columna 0"""
    def obtener_pascal(lista,indice,limite):
        """Basicamente la recursion devuelve una lista de listas que contiene cada
        una de las filas del triangulo de pascal hasta cierto limite, que es indicado por la fila buscada"""
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
        return [pascal_lista] + obtener_pascal(pascal_lista,len(pascal_lista),limite)
    #
    pascal = obtener_pascal([],0,fila)
    #accedo a la fila y la columna y obtengo el numero de pascal
    return pascal[fila][columna]

if __name__=='__main__':
    #deberia retornar 10
    print(pascal(5,2))