# arbolado-en-espacios-verdes
import csv
from collections import Counter
import os
import matplotlib.pyplot as plt

def leer_parque(nombre_archivo, parque):
    with open(nombre_archivo, encoding='utf-8') as csvfile:
        #reader = csv.DictReader(csvfile)
        reader = csv.reader(csvfile)
        headers = next(reader)
        lista = []
        for arbol in reader:
            if arbol[10] == parque:
                un_arbol = dict(zip(headers,arbol))
                lista.append(un_arbol)
            else:
                continue
    return lista

def leer_arboles(nombre_archivo):
    with open(nombre_archivo, encoding='utf-8') as archivo:
        arboles = csv.reader(archivo)
        headers = next(arboles)
        lista = [dict(zip(headers,arbol)) for arbol in arboles]
        for arbol in arboles:
            un_arbol = dict(zip(headers,arbol))
            lista.append(un_arbol)
    return lista


def especies(lista_arboles):
    lista_especies = []
    for arbol in lista_arboles:
        lista_especies.append(arbol['nombre_com'])
    return list(set(lista_especies))

def contar_ejemplares(lista_arboles):
    contadores = []
    especies_a = especies(lista_arboles)
    for especie in especies_a:
        contador_especie = 0
        for arbol in lista_arboles:
            if arbol['nombre_com'] == especie:
                contador_especie += 1
            else:
                continue
        contadores.append(contador_especie)
    diccionario = Counter()
    for indice in range(0,len(contadores)):
        diccionario[especies_a[indice]] += contadores[indice]
    
    return diccionario

def mostrar_altura(lista,nombre):
    print(nombre)
    print(f"{'-'*20}")
    print(f"Maximo: {max(lista)}")
    print(f"Promedio: {(sum(lista)/len(lista)):>.2f}\n")

def mostrar_parque(parque,nombre):
    print(nombre)
    print(f"{'-'*20}")
    for clave,valor in parque:
        print(f"{clave}: {valor}")
    print("\n")

def obtener_alturas(lista_arboles, especie):
    alturas = []
    for arbol in lista_arboles:
        if arbol['nombre_com'] == especie:
            alturas.append(float(arbol['altura_tot']))
        else:
            continue
    return alturas

def obtener_inclinaciones(lista_arboles, especie):
    inclinaciones = []
    for arbol in lista_arboles:
        if arbol['nombre_com'] == especie:
            inclinaciones.append(int(arbol['inclinacio']))
        else:
            continue
    return inclinaciones

def especimen_mas_inclinado(lista_arboles):
    lista_especies = especies(lista_arboles)
    especimen_max = ''
    inclinacion = 0
    for especimen in lista_especies:
        maximo = max(obtener_inclinaciones(lista_arboles,especimen))
        if(maximo > inclinacion):
            inclinacion = maximo
            especimen_max = especimen
        else:
            continue
    return (especimen_max,inclinacion)

def prom_lista(lista):
    return sum(lista)/len(lista)

def especie_promedio_mas_inclinada(lista_arboles):
    lista_especies = especies(lista_arboles)
    especimen_prom = ''
    promedio_max = 0.0
    for especimen in lista_especies:
        promedio = prom_lista(obtener_inclinaciones(lista_arboles,especimen))
        if promedio > promedio_max:
            especimen_prom = especimen
            promedio_max = promedio
        else:
            continue
    return (especimen_prom,promedio_max)

def medidas_de_especies(especies,arboleda):
    diccionario = {especie:[(float(arbol['altura_tot']),float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com']==especie] for especie in especies}
    """
    for especie in especies:
        medidas = [(float(arbol['altura_tot']),float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com']==especie]
        diccionario.update({especie : medidas})
    """
    return diccionario

def alturas_de_especie(arboleda,especie):
    altos = [float(arbol['altura_tot']) for arbol in arboleda if arbol['nombre_com']==especie]
    return altos
def histograma_de_altos_de_jacaranda():
    nombre_archivo = os.path.join('..', 'Data', 'arbolado-en-espacios-verdes.csv')
    arboleda = leer_arboles(nombre_archivo)
    altos = alturas_de_especie(arboleda,'Jacarandá')
    plt.hist(altos,bins=50)
    plt.show()

def alturas(tuplas):
    return [altura for altura,diametro in tuplas]
def diametros(tuplas):
    return [diametro for altura,diametro in tuplas]
def scatter_hd(lista_de_pares):
    h= alturas(lista_de_pares)
    d= diametros(lista_de_pares)
    plt.scatter(d,h)
    plt.xlabel("diametro (cm)")
    plt.ylabel("alto (m)")
    plt.title("Relación diámetro-alto para Jacarandás")
    plt.show()

def scatterplot():
    arboleda = leer_arboles('../Data/arbolado-en-espacios-verdes.csv')
    especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
    medidas = medidas_de_especies(especies,arboleda)
    for especie in especies:
        h = alturas(medidas[especie])
        d = diametros(medidas[especie])
        plt.scatter(d,h)
        plt.xlabel("diametro (cm)")
        plt.ylabel("alto (m)")
        plt.title(f"Relación diámetro-alto para {especie}")
        plt.show()

arboleda = leer_arboles('../Data/arbolado-en-espacios-verdes.csv')
#H = [float(arbol['altura_tot']) for arbol in arboleda if arbol['nombre_com']=='Jacarandá']
#print(medidas_de_especies(['Eucalipto', 'Palo borracho rosado', 'Jacarandá'],arboleda))


if __name__ == "__main__":
    scatterplot()
    """
    especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
    datos = medidas_de_especies(especies,arboleda)
    scatter_hd(datos['Jacarandá'])
    """