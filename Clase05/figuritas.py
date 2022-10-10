import random
import numpy as np
import matplotlib.pyplot as plt
def crear_album(figus_total):
    lista = [0 for i in range(figus_total)]#crea una lista de 0 de longitud figus_total
    vector = np.array(lista)#creo un vector con la lista 
    return vector
def album_incompleto(A):
    return len(A[(A==0)]) > 0 # A[(A==0)] devuelve las posiciones de 0 en el vector por lo que si su longitud es 0 indica que no hay mas figuras 
#===============================================================================================================================================
def comprar_figu(figus_total):
    figura = random.randint(1,figus_total)-1 #Posicion en el vector
    return figura
def cuantas_figus(figus_total):
    cont = 0 #lleva la cuenta de figuras compradas
    album = crear_album(figus_total)
    while album_incompleto(album):
        album[comprar_figu(figus_total)] += 1 #compra una figura y suma uno a su posicion
        cont += 1
    return cont
#================================================================================================================================================
def comprar_paquete(figus_total, figus_paquete):
    paquete = [random.randint(1,figus_total)-1 for i in range(figus_paquete)]
    return paquete
def cuantos_paquetes(figus_total, figus_paquete):
    cont = 0 #lleva la cuenta de la cantidad de paquetes que se necesita
    album = crear_album(figus_total)
    while album_incompleto(album):
        paquete = comprar_paquete(figus_total,figus_paquete)
        cont += 1
        for figura in paquete:
             album[figura] += 1 #compra una figura y suma uno a su posicion
    return cont   


def experimento_figus(n_repeticiones, figus_total):
    lista = [cuantas_figus(figus_total) for i in range(n_repeticiones)] #crea una lista con la cantidad de figuras que hay que comprar por cada iteracion 
    vector = np.array(lista) #asigno la lista al vector
    promedio =np.mean(vector) #obtengo el promedio usando mean una funcion del modulo numpy
    return promedio
def experimento_paquetes(n_repeticiones, figus_total,figus_paquete):
    lista = [cuantos_paquetes(figus_total,figus_paquete) for i in range(n_repeticiones)]
    vector = np.array(lista)
    return vector

def calcular_historia_figus_pegadas(figus_total, figus_paquete):
    album = crear_album(figus_total)
    historia_figus_pegadas = [0]
    while album_incompleto(album):
        paquete = comprar_paquete(figus_total, figus_paquete)
        while paquete:
            album[paquete.pop()] = 1
        figus_pegadas = (album>0).sum()
        historia_figus_pegadas.append(figus_pegadas)        
    return historia_figus_pegadas

if __name__=="__main__":
    #print(experimento_figus(100,670))
    #cuantos_paquetes(20,5)
    n_paquetes_hasta_llenar = experimento_paquetes(100,670,5)
    longitud = np.size(n_paquetes_hasta_llenar)
    print((n_paquetes_hasta_llenar <= 850).sum()/longitud)
    """
    figus_total = 670
    figus_paquete = 5

    plt.plot(calcular_historia_figus_pegadas(figus_total, figus_paquete))
    plt.xlabel("Cantidad de paquetes comprados.")
    plt.ylabel("Cantidad de figuritas pegadas.")
    plt.title("La curva de llenado se desacelera al final")
    plt.show()
    """