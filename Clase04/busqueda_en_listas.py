
#devuelve la posicion de un elemento en la lista
def buscar_u_elemento(lista,elemento):
    pos = -1  
    for i, z in enumerate(lista): 
        if z == elemento:   
            pos = i  
    return pos   

#devuelve la cantidad que hay de"elemento" en la lista
def buscar_n_elemento(lista,elemento):
    cont = 0 # comienzo suponiendo que no hay elementos iguales
    for x in lista:
        if x == elemento:
            cont += 1
    return  cont

def maximo(lista):
    mayor = lista[0]
    for x in lista:
        if x > mayor:
            mayor = x
    return mayor

def minimo(lista):
    menor = lista[0]
    for x in lista:
        if x < menor:
            menor = x
    return menor

if __name__ == "__main__":
    lista = [1,2,3,2,3,4]
    print(f"buscar_u_elemento({lista},1) >>> {buscar_u_elemento([1,2,3,2,3,4],1)}")
    print(f"buscar_u_elemento({lista},2) >>> {buscar_u_elemento([1,2,3,2,3,4],2)}")
    print(f"buscar_u_elemento({lista},3) >>> {buscar_u_elemento([1,2,3,2,3,4],3)}")
    print(f"buscar_u_elemento({lista},5) >>> {buscar_u_elemento([1,2,3,2,3,4],5)}")
    print(f"{'='*50}")
    print(f"buscar_n_elemento({lista},1) se repite {buscar_n_elemento([1,2,3,2,3,4],1)}")
    print(f"buscar_n_elemento({lista},2) se repite {buscar_n_elemento([1,2,3,2,3,4],2)}")
    print(f"buscar_n_elemento({lista},3) se repite {buscar_n_elemento([1,2,3,2,3,4],3)}")
    print(f"{'='*50}")
    print(f"el maximo([1,2,7,2,3,4]) es: {maximo([1,2,7,2,3,4])}")
    print(f"el maximo([1,2,3,4]) es: {maximo([1,2,3,4])}")
    print(f"el maximo([-5,4]) es: {maximo([-5,4])}")
    print(f"el maximo([-5,-4]) es: {maximo([-5,-4])}")
    print(f"{'='*50}")
    print(f"el minimo([1,2,7,2,3,4]) es: {minimo([1,2,7,0,3,4])}")
    print(f"el minimo([1,2,3,-2,4]) es: {minimo([1,2,3,-2,4])}")
    print(f"el minimo([0,-5,4]) es: {minimo([0,-5,4])}")
    print(f"el minimo([1,0,-5,-4]) es: {minimo([1,0,-5,-4])}")
    print(f"{'='*50}")