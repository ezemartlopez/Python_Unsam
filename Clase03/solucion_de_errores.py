#Solucion_de_errores.py
#Ejercicios de errores en el codigo
#%%
#Ejercicio 3.1. Función tiene_a()
#Comentario: El error era de tipo semantico y estaba ubicado dentro
#            del while despues de evaluar el if, si la primera letra
#            de la expresion no es una 'a' lo envia al else, retornando
#            un False 
#    Lo corregí moviendo el return False, que estaba dentro del else
#    hacia fuera del while y borrando la sentencia else.
#    A continuación va el código corregido
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        i += 1
    return False

tiene_a('UNSAM 2020')
tiene_a('abracadabra')
tiene_a('La novela 1984 de George Orwell')
#%%
#Ejercicio 3.2. Función tiene_a(), nuevamente
#Comentario: Los errores eran de sintaxis y estaban ubicados en:
#      def tiene_a(expresion) le falta terminar la expresion con ':'
#      while i<n le falta terminar la expresion con ':'
#      if expresion[i] = 'a' en esta expresion la comparacion de valores es equivocada va un '==' y terminar con ':'
#      return Falso  esta mal escrito la palabra reservada False

#    A continuación va el código corregido
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        i += 1
    return False

tiene_a('UNSAM 2020')
tiene_a('La novela 1984 de George Orwell')

#%%
#Ejercicio 3.3. Función tiene_uno()
#Comentario: El error era en tiempo de ejecucuion y estaba 
#ubicado basandonos en el traceback en 'n = len(expresion)'
#al leer un valor entero suelta un error, ya que un objeto
#de tipo INT no tiene uso de la funcion len() ya que no es una secuencia de datos.
#Se arregla cambiando el valor entero a un string
#    A continuación va el código corregido
def tiene_uno(expresion):
    n = len(expresion)
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if expresion[i] == '1':
            tiene = True
        i += 1
    return tiene


tiene_uno('UNSAM 2020')
tiene_uno('La novela 1984 de George Orwell')
tiene_uno('1984')

#%%
#Ejercicio 3.4. Función suma()
#Comentario: El error es de tipo semantico y se dentro de la
#unica linea de la funcion suma()
#   c = a + b
# se arreglaria usando return de los valores a y b 
#    A continuación va el código corregido
def suma(a,b):
    return a + b

a = 2
b = 3
c = suma(a,b)
print(f"La suma da {a} + {b} = {c}")

#%%
#Ejercicio 3.5. Pisando Memoria
#Comentario: el es del tipo semantico ya que el error radica
# en que cada elemento de la lista hace referencia al mismo objeto, es decir 
# a medida que se un objeto se lo formatea asignando la fila que se lee
# y se inserta en la lista, y como se usa una variable una misma variable,
# todos los elementos de la lista hacen referencia al mismo objeto, entonces
# todos los elementos de la lista se modifican
# al ultimo valor que se asigna a la variable registro 
#   La solucion es definir la variable registro dentro del bucle for de modo que cada
#vez que se itere en el bucle se use una nueva variable registro, de modo que ningun elemento
#de la lista haga referencia al mismo objeto.
#    A continuación va el código corregido
import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]
    registro={}
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro={}
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            
            camion.append(registro)
    return camion

camion = leer_camion('../Data/camion.csv')
pprint(camion)