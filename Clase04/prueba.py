

def tribonacci(lista,n):
    datos = []
    aux = lista.copy()
    cont = 0
    m = 0
    while cont < n:
        if len(datos) < 3:
            datos.append((aux[cont]))
        else:
            suma = datos[m]+datos[m+1]+datos[m+2]
            
            datos.append(suma)
            m += 1
        cont += 1
    
    return datos

#print(tribonacci([0.5, 0.5, 0.5], 30))
