# arbolado-en-espacios-verdes
import csv
from collections import Counter

def leer_parque(nombre_archivo, parque):
    """Lee el archivo y devuelve una lista de diccionarios de todos los arboles que estan en un parque especifico"""
    with open(nombre_archivo, encoding='utf-8') as csvfile:
        #reader = csv.DictReader(csvfile)
        reader = csv.reader(csvfile)
        headers = next(reader) #obtengo las cabeceras del archivo
        lista = []
        for arbol in reader:
            if arbol[10] == parque:
                un_arbol = dict(zip(headers,arbol)) #creo un diccionario del arbol
                lista.append(un_arbol)
            else: #en caso de encontrar una excepcion solo pasa de largo
                continue
    return lista
 

def especies(lista_arboles):
    """Lee una lista de diccionarios(un arbol con sus datos cada uno) y devuelve una lista con los nombres de las especies sin repetir"""
    lista_especies = []
    for arbol in lista_arboles:
        lista_especies.append(arbol['nombre_com'])
    return list(set(lista_especies))

def contar_ejemplares(lista_arboles):
    """dada una lista como la que generada con leer_parque(), devuelva un diccionario en el que las especies sean las claves y tengan como valores asociados la cantidad de ejemplares en esa especie en la lista dada."""
    especies_a = especies(lista_arboles)
    contadores = [] #guarda los contadores de cada arbol segun la especie
    for especie in especies_a:
        contador_especie = 0 #contador de una especie en lista_arboles
        for arbol in lista_arboles:
            if arbol['nombre_com'] == especie:
                contador_especie += 1
            else:
                continue
        contadores.append(contador_especie)
    #NOTA: el indice de posicion de cada especie en la lista especies_a,
    #      coincide con el indice respecto ala cantidad que hay de esa especie
    diccionario = Counter()
    for indice in range(0,len(contadores)):
        diccionario[especies_a[indice]] += contadores[indice]
    
    return diccionario

def mostrar_altura(lista,nombre):
    """De una lista de alturas y un nombre de un parque, imprime el maximo y el promedio de alturas"""
    print(nombre)
    print(f"{'-'*20}")
    print(f"Maximo: {max(lista)}")
    print(f"Promedio: {(sum(lista)/len(lista)):>.2f}\n")

def mostrar_parque(parque,nombre):
    """De una lista con los 5 ejemplares que mas se repiten, imprime el la especie y la cantidad de cada arbol en la lista"""
    print(nombre)
    print(f"{'-'*20}")
    for clave,valor in parque:
        print(f"{clave}: {valor}")
    print("\n")

def obtener_alturas(lista_arboles, especie):
    """dada una lista de árboles como la anterior y una especie de árbol (columna 'nombre_com' del archivo),
    devuelva una lista con las alturas (columna 'altura_tot') de los ejemplares de esa especie en la lista."""
    alturas = []
    for arbol in lista_arboles:
        if arbol['nombre_com'] == especie:
            alturas.append(float(arbol['altura_tot']))
        else:
            continue
    return alturas

def obtener_inclinaciones(lista_arboles, especie):
    """que, dada una especie de árbol y una lista de árboles como la anterior, devuelva una lista con las inclinaciones (columna 'inclinacio') de los ejemplares de esa especie."""
    inclinaciones = []
    for arbol in lista_arboles:
        if arbol['nombre_com'] == especie:
            inclinaciones.append(int(arbol['inclinacio']))
        else:
            continue
    return inclinaciones

def especimen_mas_inclinado(lista_arboles):
    """dada una lista de árboles devuelva la especie que tiene el ejemplar más inclinado y su inclinación."""
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
    """ dada una lista de árboles devuelva la especie que en promedio tiene la mayor inclinación y el promedio calculado en una tupla"""
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

if __name__=="__main__":
    nombre_archivo = '../Data/arbolado-en-espacios-verdes.csv'
    parque = 'GENERAL PAZ'
    parque_andes = 'ANDES, LOS'
    parque_centenario = 'CENTENARIO'

    lista_gralpaz = leer_parque(nombre_archivo,parque)
    lista_andes = leer_parque(nombre_archivo,parque_andes)
    lista_centenario = leer_parque(nombre_archivo,parque_centenario)

    #******************************************************************************************

    print("Ejercicio 3.18: Lectura de los árboles de un parque")
    #print(lista_gralpaz)#COMO UCUPARIA DEMASIADA PANTALLA OPTE POR MOSTRAR SOLO LA LONGITUD, PERO SE PUEDE MOSTRAR DESCOMENTANDO ESTA LINEA
    print(f"Cantidad de arboles en parque {parque} es de: {len(lista_gralpaz)}")
    print(f"Cantidad de arboles en parque {parque_andes} es de: {len(lista_andes)}")
    print(f"Cantidad de arboles en parque {parque_centenario} es de: {len(lista_centenario)}\n")

    #******************************************************************************************

    print("Ejercicio 3.19: Determinar las especies en un parque\n")
    especies_gralpaz = especies(lista_gralpaz)
    #print(especies_gralpaz)#COMO UCUPARIA DEMASIADA PANTALLA OPTE POR MOSTRAR SOLO LA LONGITUD, PERO SE PUEDE MOSTRAR DESCOMENTANDO ESTA LINEA
    print(f"Cantidad de especies en parque {parque} es de: {len(especies_gralpaz)}\n")

    #******************************************************************************************

    print("Ejercicio 3.20: Contar ejemplares por especie\n")
    mas_comunes_gral = contar_ejemplares(lista_gralpaz)
    mas_comunes_andes = contar_ejemplares(lista_andes)
    mas_comunes_centenario = contar_ejemplares(lista_centenario)
    general_paz_comunes = mas_comunes_gral.most_common(5)
    andes_comunes = mas_comunes_andes.most_common(5)
    centenario_comunes = mas_comunes_centenario.most_common(5)

    mostrar_parque(general_paz_comunes,parque)

    mostrar_parque(andes_comunes,'Los Andes')

    mostrar_parque(centenario_comunes,parque_centenario)

    #******************************************************************************************

    print("Ejercicio 3.21: Alturas de una especie en una lista\n")
    alturas_gral = obtener_alturas(lista_gralpaz,'Jacarandá')
    alturas_andes = obtener_alturas(lista_andes,'Jacarandá')
    alturas_centenario = obtener_alturas(lista_centenario,'Jacarandá')
    mostrar_altura(alturas_gral,parque)
    mostrar_altura(alturas_andes,'Los Andes')
    mostrar_altura(alturas_centenario,parque_centenario)

    #******************************************************************************************

    print("Ejercicio 3.23: Especie con el ejemplar más inclinado\n")
    t_gralPaz = especimen_mas_inclinado(lista_gralpaz)
    t_andes = especimen_mas_inclinado(lista_andes)
    t_centenario = especimen_mas_inclinado(lista_centenario)
    print(f"Parque {parque} el especimen mas inclinado es: {t_gralPaz[0]} con {t_gralPaz[1]} grados")
    print(f"Parque Los Andes el especimen mas inclinado es: {t_andes[0]} con {t_andes[1]} grados")
    print(f"Parque {parque_centenario} el especimen mas inclinado es: {t_centenario[0]} con {t_centenario[1]} grados\n")

    #******************************************************************************************

    print("Ejercicio 3.24: Especie más inclinada en promedio\n")
    tupla_andes = especie_promedio_mas_inclinada(lista_andes)
    print(f"Parque Los Andes el especimen mas inclinado en promedio es: {tupla_andes[0]} con {tupla_andes[1]} grados")
