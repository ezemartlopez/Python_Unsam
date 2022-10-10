import numpy as np
import matplotlib.pyplot as plt

def randomwalk(largo):
    pasos=np.random.randint (-1,2,largo)    
    return pasos.cumsum()
def lista_abs(lista):
    largo = lista.size
    for i in range(largo):
        lista[i] = abs(lista[i])
    
    return lista

def maximo(lista):
    """Devuelve el maximo de uan lista numpy"""
    aux = np.copy(lista)
    maximo = np.max(lista_abs(aux))#max(abs(np.cumsum(lista)))
    return maximo

def view_only(tupla):
    """Solo ve la primera parte de la tupla para la comparacion de list.sort"""
    return tupla[0]

def ordenar_caminatas(caminatas):
    """Ordena las caminatas teniendo en cuenta cual se aleja mas del camino,
    es decir busca cual caminata tiene un tiempo donde este mas alejada del camino respecto a otras caminatas"""
    lista = []
    #creo una tupla
    for i,caminata in enumerate(caminatas):
        tupla = (maximo(caminata),i)
        lista.append(tupla)
    #deeria ordenarlo de menor a mayor los maximos con sus indices
    lista.sort(key=view_only)
    new_list = []
    for tupla in lista:
        new_list.append(caminatas[tupla[1]])
    return new_list
def graficar():
    N = 100000
    trayectorias = 12
    #======================================
    plt.figure()
    plt.subplot(2, 1, 1) #Plot superior
    plt.xlabel("Tiempo")
    plt.ylabel("Distancia al origen")
    plt.title("12 caminatas al azar")
    caminatas = [randomwalk(N) for i in range(trayectorias)]
    caminatas = ordenar_caminatas(caminatas)
    mas_alejado = caminatas[-1]
    menos_alejado = caminatas[0]
    for caminata in caminatas:
        plt.plot(caminata)
    
    plt.subplot(2,2,3) #Plot inferior izquierda
    plt.title("la caminata que mas se aleja")
    plt.plot(mas_alejado,color='r')

    plt.subplot(2,2,4) #Plot inferior derecha
    plt.title("la caminata que menos se aleja")
    plt.plot(menos_alejado)
    plt.show()
    

if __name__=="__main__":
    graficar()