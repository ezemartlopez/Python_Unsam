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
    return lista

if __name__=='__main__':
    lista_1 = [5,4,3,2,1]
    print(f"\nLa lista comienza en: {lista_1}")
    print(ord_burbujeo(lista_1,debug=True))


    lista_2 = [1, 2, 3, 4, 5]
    print(f"\nLa lista comienza en: {lista_2}")
    print(ord_burbujeo(lista_2,debug=True))


    lista_3 = [0, 9, 3, 8, 5, 3, 2, 4]
    print(f"\nLa lista comienza en: {lista_3}")
    print(ord_burbujeo(lista_3,debug=True))


    lista_4 = [10, 8, 6, 2, -2, -5]
    print(f"\nLa lista comienza en: {lista_4}")
    print(ord_burbujeo(lista_4,debug=True))


    lista_5 = [2, 5, 1, 0]
    print(f"\nLa lista comienza en: {lista_5}")
    print(ord_burbujeo(lista_5,debug=True))
