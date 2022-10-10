import random
import numpy as np
def medir_temp(n):
    media = 0
    desviacion = 0.2
    temperatura = 37.5
    lista = []
    for i in range(n):
        lista.append(temperatura + random.normalvariate(media,desviacion))
    a = np.array(lista)
    np.save('../Data/temperatura.npy',a)
    return lista
def minimo(lista):
    return min(lista)
def maximo(lista):
    return max(lista)
def promedio(lista):
    return sum(lista)/len(lista)
def mediana(lista):
    lista.sort()
    mediana = 0
    if len(lista) % 2 == 0:
        pos = int(len(lista)/2)
        mediana = (lista[pos] + lista[pos - 1])/2
    else:
        pos = int(len(lista)/2)
        mediana = lista[pos]
    return mediana

def cuartiles(lista):
    lista.sort()
    n = len(lista)
    primer_cuartil = 0
    seg_cuartil = 0
    tercer_cuartil = 0
    #Calculo del primer cuartil
    if (n+1) % 4 == 0:
        pos = int((n+1)/4)-1
        primer_cuartil = lista[pos]
    else:
        pos = int((n+1)/4)-1
        primer_cuartil = lista[pos]+0.25*(lista[pos+1]-lista[pos])
    #Calculo del segundo cuartil con la mediana
    seg_cuartil = mediana(lista)
    #Calculo del tercer cuartil
    if (3*(n+1)) % 4 == 0:
        pos = int(3*(n+1)/4)-1
        tercer_cuartil = lista[pos]
    else:
        pos = int(3*(n+1)/4)-1
        tercer_cuartil = lista[pos]+0.75*(lista[pos+1]-lista[pos])
    
    return [primer_cuartil,seg_cuartil,tercer_cuartil]

def resumen_temp(n):
    lista = medir_temp(n)
    tupla = (maximo(lista),minimo(lista),promedio(lista),mediana(lista))
    return tupla

if __name__ == "__main__":
    print(resumen_temp(999))
    print(cuartiles([19,21,24,28,28,29,30,32,33,34,37,40,45,45,52,53,54,56,60,63]))