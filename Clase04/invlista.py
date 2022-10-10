def invertir_lista(lista):
    invertida = []
    for e in lista: # Recorro la lista
        invertida = [e] + invertida #agrego el elemento e al principio de la lista invertida y lo uno con lo que habia antes en invertida
    return invertida


if __name__ == "__main__":
    lista1 = [1, 2, 3, 4, 5]
    lista2 = ['Bogotá','Rosario','Santiago','San Fernando','San Miguel']
    print(invertir_lista(lista1))
    print(invertir_lista(lista2))

