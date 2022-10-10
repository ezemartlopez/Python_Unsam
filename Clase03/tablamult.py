def s_fmt(value):
    """Toma un valor entero y lo convierte a una cadena de largo 4"""
    return '%4d' % value
def n_fila(num):
    """Devuelve una cadena que seria el comienzo de cada fila de la tabla de multiplicacion del numero (num)"""
    var ='%d' % num
    #Ejemplo: devuelve "3:   "
    return var+':'+' '*(4-len(var))

#Basicamente regresa una cadena que contiene
def fila_tabla(comienzo,paso):
    """Devuelve cada fila(formato string) de la tabla de multiplicacion siguiendo el paso establecido,
    es decir realiza la multiplcacion con sumas sucesivas"""
    cadena = comienzo #comienzo fila de la tabla
    multiplos = [0]#tabla con los multiplos
    suma = 0
    for n in range(1,10):
        suma += paso
        multiplos.append(suma)
    for num in range(0,10):
        cadena += s_fmt(multiplos[num])
    return cadena
 
def imprimir_tabla():
    encabezado = fila_tabla('     ',1)#encabezado de la tabla
    print(encabezado)
    print(f"{'-'*(len(encabezado))}")
    for paso in range(0,10):
        comienzo = n_fila(paso)
        print(fila_tabla(comienzo,paso))
        
if __name__=="__main__":
    imprimir_tabla()