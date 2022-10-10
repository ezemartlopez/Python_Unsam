
#%%
import numpy as np
from collections import Counter

def completar_tirada(seleccion):
    '''recibe los dados que se guardaron de una tirada anterior
    y completa tirando los que falta hasta 5'''
    tirada = seleccion
    while len(tirada)<5:
        tirada.append(np.random.randint(1,7))
    return tirada

def seleccionar_mejores(tirada):
    '''selecciona los dados que más se repiten 
    en una tirada dada.
    '''
    #cuento repeticiones
    T=Counter(tirada)

    #me fijo cual es el dado que más tengo
    d=T.most_common(1)[0][0] #dado que más se repite
    n=T.most_common(1)[0][1] #cuantas veces se repite
    
    #esos los selecciono para la próxima mano
    seleccion =[d]*n

    return seleccion


#%%


N=100000   # vamos a jugar N manos de generala, cada una hasta 3 tiradas.
generalas=0 # cuento las generalas que saco

for j in range(N):
    if j%10000==0:
        print(j)
    seleccion = [] #comienzo sin dados "seleccionados"
    for k in range(3):
        tirada = completar_tirada(seleccion) #completo tirando los dados que falten
        seleccion = seleccionar_mejores(tirada) # selecciono los repetidos
 
    #luego de las tres manos, si tengo 5 iguales, hice generala
    if len(seleccion) == 5:
        generalas += 1
        
print(f"Probabilidad de obtener generala haciendo mi mejor esfuerzo: {100*generalas/N}%")

#%%
