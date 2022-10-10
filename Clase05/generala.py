import random
import collections
def todos_distintos(lista):
    var = True
    lista.sort()
    prueba = 0 #asumo que todos son >=1 y <=6
    for dado in lista:
        if dado > prueba:
            prueba = dado
        else:
            var = False
            break
    return var


def mas_repetido(lista):
    tirada = collections.Counter()#uso esta colleccion para no recurrir a funciones complejas
    tirada.update(lista)#lo cargo ala coleccion
    l = tirada.most_common(1)#obtengo el mas repetido
    t = l[0]
    return t[0]
def remover(lista,valor):
    aux =[value for value in lista if value != valor]
    return aux
def tirar():
    tirada = []
    for i in range(5):
        tirada.append(random.randint(1,6))
    return tirada

def tirar_n_dados(numero):
    tirada = [random.randint(1,6) for i in range(numero)]
    return tirada

def es_generala(tirada):
    tiro = tirada[0]#asumo que hay por lo menos un tiro
    #si la long. de tirada es de la misma cantidad que la cantidad de tiros que hay en la lista
    return len(tirada) == tirada.count(tiro)

def tiro_no_necesariamente_servido():
    puedo_repetir = 2 #numero de veces que puedo tirar los dados
    tirada = tirar()#obtengo un tiro cualquiera
    if todos_distintos(tirada):
        mas_comun = tirada[random.randint(0,4)]
        puedo_repetir -= 1
    else:
        mas_comun = mas_repetido(tirada)
    

    tirada = remover(tirada,mas_comun)#quito al mas repetido

    for i in range(puedo_repetir):
        tiro = tirar_n_dados(len(tirada))
        tirada = [dado for dado in tiro if dado !=mas_comun]
    aux = tirada + [mas_comun for n in range(5-len(tirada))]
    return aux

def prob_generala(N):
    G = sum([es_generala(tiro_no_necesariamente_servido()) for i in range(N)])
    prob = G/N
    print(f'Tiré {N} veces, de las cuales {G} saqué generala servida.')
    print(f'Podemos estimar la probabilidad de sacar generala servida mediante {prob:.6f}.')

if __name__ == "__main__":
    prob_generala(10000)
   