#documnetacion.py
def valor_absoluto(n):
    """Devuelve el valor absoluto de un numero"""
    if n >= 0:
        return n
    else:
        return -n


def suma_pares(l):
    """Calcula la sumatoria de todos los numeros pares en una lista"""
    res = 0
    for e in l:
        if e % 2 ==0:
            res += e
        else:
            res += 0

    return res
    #Para este caso la invariante de ciclo es la variable res que contiene la sumatoria de los numeros pares



def veces(a, b):
    """Devuelve la suma de b veces el valor de a
       Pre: a debe ser un numero entero o decimal y b debe ser entero mayor a cero
       Pos: devuelve la suma de b veces el valor de a
    """
    res = 0
    nb = b #numero de veces repite ciclo
    #continuo el ciclo hasta que se vuelva cero nb. Ojo ver precondiciones
    while nb != 0:
        #print(nb * a + res)
        res += a
        nb -= 1
    return res
    #Para este caso la invariante de ciclo es la variable res que contiene la sumatoria repeticiones de a


def collatz(n):
    """Devuelve el numero de veces que puede dividir por 2 siempre con un resto igual a cero, hasta llegar a uno.

    Pre: n debe ser un entero mayor a cero
    Pos: devuelve el numero de veces que lo divide por dos siempre con un resto igual a cero
    """
    res = 1 #almacena la cantidad de divisiones por 2 que se realiza mas uno

    while n!=1:
        if n % 2 == 0:
            n = n//2
        else:
            #como no es divisible por 2, lo multiplica por 3 y le suma uno, convirtiendolo en par divisible por 2
            n = 3 * n + 1
        #print(f"n vale: {n}")
        res += 1

    return res
    #la invariante del ciclo es la variable res que contiene las veces que divide a n

if __name__=="__main__":
    print(collatz(4))
    print(collatz(3))