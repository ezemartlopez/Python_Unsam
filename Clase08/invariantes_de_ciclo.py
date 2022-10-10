##  Invariantes de ciclo
"""
Los invariantes se refieren a estados o condiciones que no cambian dentro de un contexto o porción de código. Hay invariantes de ciclo, que son los que veremos a continuación, e invariantes de estado, que se verán más adelante.
Los invariantes se refieren a estados o situaciones que no cambian dentro de un contexto dado. Hay diferentes tipos de invariantes. A continuación veremos los invariantes de ciclo que nos ayudan a llegar desde las precondiciones hasta las postcondiciones.

Un invariante de ciclo es una aseveración que debe ser verdadera al comienzo de cada iteración del ciclo y al salir del mismo.
Un _invariante_ de ciclo es esencialmente una aseveración que debe ser verdadera al final de cada iteración. Pensar en términos de invariantes de ciclo nos ayuda a reflexionar y comprender mejor qué es lo que debe realizar nuestro código y nos ayuda a desarrollarlo.

Por ejemplo, si el problema es ir desde el punto A al punto B, la precondición dice que tenemos que estar parados en A y la poscondición que al terminar estaremos parados en B. En este caso las siguientes aseveraciones son invariantes: "estamos en algún punto entre A y B", "estamos en el punto más cercano a B que estuvimos hasta ahora". Son aseveraciones que podría tener nuestro código (y dependen exclusivamente de cómo lo programamos).

Pensar en términos de invariantes de ciclo nos ayuda a reflexionar y comprender mejor qué es lo que debe realizar nuestro código y nos ayuda a desarrollarlo.

Por ejemplo, para la función `maximo`, que busca el valor más grande de una lista desordenada, podemos enunciar:
- precondición: la lista contiene elementos que tienen una relación de orden (son comparables con <)
- poscondición: se devolverá el elemento máximo de la lista, si es que tiene elementos, y si no se devolverá None.
Veamos un ejemplo: supongamos que analizamos un ciclo que buscar el máximo en una lista no necesariamente ordenada. La precondición es que la lista es no vacía y contiene elementos que son comparables y la postcondición es que se devuelve el elemento máximo de la lista. Por convención, diremos que el máximo de una lista vacía es menos infinito.

#Codigo python
import math
def maximo(lista):
    'Devuelve el elemento máximo de la lista o None si está vacía.'
    if not lista:
        return None
    max_elem = lista[0]
    '''
    Pre: La lista contiene elementos comparable entre sí y con math.inf
    Pos: La función devuelve el elemento máximo de la lista.
    '''
    max_elem = -math.inf
    for elemento in lista:
        if elemento > max_elem:
            max_elem = elemento
    return max_elem
"""